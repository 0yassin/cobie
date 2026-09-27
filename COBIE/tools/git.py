from tools.terminal import run_command

def git_status():
    return run_command("git status")

def git_diff():
    return run_command("git diff")