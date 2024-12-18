from ..enums.statcast_leaderboard import Hand


def get_hand_param_str(hand: str | Hand) -> str:
    if not isinstance(hand, str) and not isinstance(hand, Hand):
        raise ValueError(f'Invalid type for hand: {type(hand)}')

    if not Hand.has_value(hand):
        raise ValueError(f'Invalid hand: {hand}')

    return f'{hand}'


def get_prior_pk_param_str(prior_pk: str) -> str:
    if not isinstance(prior_pk, str):
        raise ValueError(f'Invalid type for prior_pk: {type(prior_pk)}')

    if prior_pk not in ['all', '1', '2', '3']:
        raise ValueError(f'Invalid prior_pk: {prior_pk}')

    return prior_pk
