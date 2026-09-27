"""Check browser-observed session setup for Technicolor PBKDF2 entries."""

from __future__ import annotations

import pytest
from solentlabs.cable_modem_monitor_catalog import CATALOG_PATH
from solentlabs.cable_modem_monitor_core.config_loader import load_modem_config

SESSION_CASES = ("cga4236", "cga6444vf")


@pytest.mark.parametrize("model_dir", SESSION_CASES)
def test_pbkdf2_session_establishment(model_dir: str) -> None:
    """Catalog entries declare the browser headers and post-login menu call."""
    config = load_modem_config(CATALOG_PATH / "technicolor" / model_dir / "modem.yaml")

    assert config.session is not None
    assert config.session.resolved_headers(base_url="https://192.0.2.1") == {
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://192.0.2.1/",
    }
    assert config.session.post_login_endpoints == ["/api/v1/session/menu"]
