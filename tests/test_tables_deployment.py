from fairderm_eval.ledger.datasets import fairness_eval_datasets, total_public_images
from fairderm_eval.orchestration.audit import headline_audit
from fairderm_eval.trial.deployment import deployment_table, workflow_table


def test_dataset_counts() -> None:
    assert len(fairness_eval_datasets()) == 5
    assert total_public_images() > 60000


def test_deployment_success() -> None:
    rows = deployment_table()
    assert rows[-1]["success"] is True
    assert workflow_table()["auto_processed"] == 96.3
    assert headline_audit()["deployment_success"] is True
