from qe_custom.paths import data_dir, project_root


def test_project_root_has_pyproject() -> None:
    assert (project_root() / "pyproject.toml").exists()


def test_data_dir_for_known_kinds() -> None:
    assert data_dir("raw").name == "raw"
    assert data_dir("processed").name == "processed"
    assert data_dir("external").name == "external"
