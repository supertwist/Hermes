import re, json, sys, subprocess

def _run_hermes_command(cmd_str):
    # Execute a hermes CLI command and capture its output.
    result = subprocess.run(['hermes', 'rhino3_run_command', cmd_str], capture_output=True, text=True)
    return {'output': result.stdout.strip(), 'error': result.stderr.strip(), 'exit_code': result.returncode}


def _parse_sphere(text):
    m = re.search(r"sphere[^\d]*([\d.]+)\s*cm\s*diameter", text, re.I)
    if not m:
        return None
    diam_cm = float(m.group(1))
    radius_mm = (diam_cm/2)*10  # Rhino uses mm by default
    return f"Sphere 0,0,0 {radius_mm:.3f}"

def _parse_box(text):
    m = re.search(r"box[^\d]*([\d.]+)\s*x\s*([\d.]+)\s*x\s*([\d.]+)\s*cm", text, re.I)
    if not m:
        return None
    x, y, z = map(lambda v: float(v)*10, m.groups())
    # Rhino command: Box <corner> <dx> <dy> <dz>
    return f"Box 0,0,0 {x:.3f} {y:.3f} {z:.3f}"

def _parse_octagon(text):
    # Look for "octagon" or "8-sided" with optional side length
    if not re.search(r"octagon|8[-\s]?sided", text, re.I):
        return None
    # Try to capture side length in cm
    m = re.search(r"side(?: length)?[^\d]*([\d.]+)\s*cm", text, re.I)
    if m:
        side_cm = float(m.group(1))
        # Approximate radius from side length: r = s / (2 * sin(pi/8))
        import math
        radius_mm = (side_cm/2) / math.sin(math.pi/8) * 10
    else:
        # default radius 10 mm
        radius_mm = 10.0
    # Rhino command: Polygon <sides> <radius>
    return f"Polygon 8 {radius_mm:.3f}"

def handle(request: str):
    cmd = (
        _parse_sphere(request) or 
        _parse_box(request) or 
        _parse_octagon(request)
    )
    if cmd:
        # Execute the Rhino command via hermes CLI
        res = _run_hermes_command(cmd)
        return {"status": "ok", "command": cmd, "output": res.get('output', ''), "error": res.get('error',''), "exit_code": res.get('exit_code')}
    # fallback: could not parse; inform user
    return {"status": "unrecognized", "message": "Could not understand request for geometry."}

if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""
    print(json.dumps(handle(q)))
