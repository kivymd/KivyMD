def test_create_project():
    import os
    import sys

    os.system(
        f"{sys.executable} -m kivymd.tools.patterns.create_project "
        f"MVC "
        f"{os.path.expanduser('~')} "
        f"TestProject "
        f"{sys.executable} "
        f"master "
        f"--name_screen TestProjectScreen "
        f"--use_firebase yes "
        f"--use_hotreload yes"
    )
    assert os.path.exists(os.path.join(os.path.expanduser("~"), "TestProject"))
