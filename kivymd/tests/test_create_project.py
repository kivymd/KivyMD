def test_create_project():
    import os

    os.system(
        f"python3.10 -m kivymd.tools.patterns.create_project "
        f"MVC "
        f"{os.path.expanduser('~')} "
        f"TestProject "
        f"python3.10 "
        f"stable "
        f"--name_screen TestProjectScreen "
        f"--name_database restdb "
        f"--use_hotreload yes"
    )
    assert os.path.exists(os.path.join(os.path.expanduser("~"), "TestProject"))
