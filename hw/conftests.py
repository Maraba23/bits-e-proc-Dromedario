#!/usr/bin/env python3

import pytest
from telemetry import telemetry


def pytest_sessionstart(session):
    session.results = []


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call":
        item.session.results.append(result._to_json())


def pytest_sessionfinish(session, exitstatus):
    t = telemetry("embarcados")
    for v in session.results:
        name = v["nodeid"].split("::")[1]
        status = t.statusOk
        log = {"id": name, "status": v["outcome"]}

        if log["status"] == "failed":
            log["msg"] = v["longrepr"]["reprcrash"]["message"]
            status = t.statusFail

        t.push(log, name, status, channel="lab-comb")
