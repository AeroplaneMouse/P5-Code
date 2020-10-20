from models.TPattern import TPattern


A = TPattern(
    {'0_20->25': ['=']}
)

B = TPattern(
    {'1_20->25': ['=']}
)

C = TPattern(
    {'2_20->25': ['=']}
)

D = TPattern(
    {'3_20->25': ['=']}
)

AB = {
    '0_20->25': ['='],
    '1_20->25': ['s', '=']
}

All = [A, B, C, D, AB]
