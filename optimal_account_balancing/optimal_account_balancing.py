from collections import defaultdict


def get_optimal_account_balancing(transactions: list[list[int]]) -> int:
    balance_per_person = defaultdict(int)

    for lender, borrower, amount in transactions:
        balance_per_person[lender] -= amount
        balance_per_person[borrower] += amount

    return get_minimum_number_of_transactions(
        balances=sorted([balance for balance in balance_per_person.values() if balance != 0]),
        start_idx=0,
    )


def get_minimum_number_of_transactions(balances: list[int], start_idx: int):
    if start_idx == len(balances):
        return 0

    current_balance = balances[start_idx]
    next_idx = start_idx + 1

    # If current balance is settled proceed to the next one
    if current_balance == 0:
        return get_minimum_number_of_transactions(balances, next_idx)

    minimum_number_of_transactions = float("inf")

    # Try to settle current balance with all remaining balances
    for to_settle_idx in range(next_idx, len(balances)):
        balance_to_settle = balances[to_settle_idx]

        # Balance to settle must be non-zero and of different sign
        if (balance_to_settle * current_balance) < 0:
            balances[to_settle_idx] += current_balance

            minimum_number_of_transactions = min(
                1 + get_minimum_number_of_transactions(balances, next_idx), minimum_number_of_transactions
            )

            balances[to_settle_idx] -= current_balance

    return minimum_number_of_transactions
