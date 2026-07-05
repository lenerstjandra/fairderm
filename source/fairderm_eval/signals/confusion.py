from collections.abc import Iterable

from fairderm_eval.typing import GroupCounts, MetricBundle


def count_binary(labels: Iterable[int], predictions: Iterable[int]) -> GroupCounts:
    tp = fp = tn = fn = 0
    for label, prediction in zip(labels, predictions, strict=True):
        if label == 1 and prediction == 1:
            tp += 1
        elif label == 0 and prediction == 1:
            fp += 1
        elif label == 0 and prediction == 0:
            tn += 1
        elif label == 1 and prediction == 0:
            fn += 1
        else:
            raise ValueError("labels and predictions must be binary")
    return GroupCounts(tp=tp, fp=fp, tn=tn, fn=fn)


def safe_div(num: float, den: float) -> float:
    if den == 0:
        return 0.0
    return num / den


def rates(counts: GroupCounts) -> MetricBundle:
    sensitivity = safe_div(counts.tp, counts.tp + counts.fn)
    specificity = safe_div(counts.tn, counts.tn + counts.fp)
    fnr = 1.0 - sensitivity
    fpr = 1.0 - specificity
    total = counts.tp + counts.fp + counts.tn + counts.fn
    accuracy = safe_div(counts.tp + counts.tn, total)
    positive_rate = safe_div(counts.tp + counts.fp, total)
    return MetricBundle(sensitivity, specificity, fnr, fpr, accuracy, positive_rate)


def merge_counts(items: Iterable[GroupCounts]) -> GroupCounts:
    tp = fp = tn = fn = 0
    for item in items:
        tp += item.tp
        fp += item.fp
        tn += item.tn
        fn += item.fn
    return GroupCounts(tp=tp, fp=fp, tn=tn, fn=fn)


def invert_counts(counts: GroupCounts) -> GroupCounts:
    return GroupCounts(tp=counts.tn, fp=counts.fn, tn=counts.tp, fn=counts.fp)
