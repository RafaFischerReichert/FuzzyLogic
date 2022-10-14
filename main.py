from time import sleep
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control

dom_velocidade = np.arange(-10, 141, 1)
dom_tensao = np.arange(-10, 251, 1)

TensaoInicial = control.Antecedent(dom_tensao, "TensaoInicial")
MudancaDeVelocidade = control.Antecedent(dom_velocidade, "MudancaDeVelocidade")

MudancaDeTensao = control.Consequent(dom_tensao, "MudancaDeTensao")

MudancaDeVelocidade["MI"] = fuzz.trapmf(MudancaDeVelocidade.universe, [-10, -10, 0, 13])
MudancaDeVelocidade["MME"] = fuzz.trimf(MudancaDeVelocidade.universe, [0, 13, 26])
MudancaDeVelocidade["MP"] = fuzz.trimf(MudancaDeVelocidade.universe, [13, 26, 39])
MudancaDeVelocidade["+/-P"] = fuzz.trimf(MudancaDeVelocidade.universe, [29, 39, 52])
MudancaDeVelocidade["PP"] = fuzz.trimf(MudancaDeVelocidade.universe, [39, 52, 65])
MudancaDeVelocidade["ME"] = fuzz.trimf(MudancaDeVelocidade.universe, [52, 65, 78])
MudancaDeVelocidade["PG"] = fuzz.trimf(MudancaDeVelocidade.universe, [65, 78, 91])
MudancaDeVelocidade["+/-G"] = fuzz.trimf(MudancaDeVelocidade.universe, [78, 91, 104])
MudancaDeVelocidade["MG"] = fuzz.trimf(MudancaDeVelocidade.universe, [91, 104, 117])
MudancaDeVelocidade["MMG"] = fuzz.trimf(MudancaDeVelocidade.universe, [104, 117, 130])
MudancaDeVelocidade["MX"] = fuzz.trapmf(
    MudancaDeVelocidade.universe, [117, 130, 140, 140]
)

TensaoInicial["MI"] = fuzz.trapmf(TensaoInicial.universe, [-10, -10, 20, 42])
TensaoInicial["MME"] = fuzz.trimf(TensaoInicial.universe, [20, 42, 64])
TensaoInicial["MP"] = fuzz.trimf(TensaoInicial.universe, [42, 64, 86])
TensaoInicial["+/-P"] = fuzz.trimf(TensaoInicial.universe, [64, 86, 108])
TensaoInicial["PP"] = fuzz.trimf(TensaoInicial.universe, [86, 108, 130])
TensaoInicial["ME"] = fuzz.trimf(TensaoInicial.universe, [108, 130, 152])
TensaoInicial["PG"] = fuzz.trimf(TensaoInicial.universe, [130, 152, 174])
TensaoInicial["+/-G"] = fuzz.trimf(TensaoInicial.universe, [152, 174, 196])
TensaoInicial["MG"] = fuzz.trimf(TensaoInicial.universe, [174, 196, 218])
TensaoInicial["MMG"] = fuzz.trimf(TensaoInicial.universe, [196, 218, 240])
TensaoInicial["MX"] = fuzz.trapmf(TensaoInicial.universe, [218, 240, 250, 250])

MudancaDeTensao["MI"] = fuzz.trapmf(MudancaDeTensao.universe, [-10, -10, 20, 42])
MudancaDeTensao["MME"] = fuzz.trimf(MudancaDeTensao.universe, [20, 42, 64])
MudancaDeTensao["MP"] = fuzz.trimf(MudancaDeTensao.universe, [42, 64, 86])
MudancaDeTensao["+/-P"] = fuzz.trimf(MudancaDeTensao.universe, [64, 86, 108])
MudancaDeTensao["PP"] = fuzz.trimf(MudancaDeTensao.universe, [86, 108, 130])
MudancaDeTensao["ME"] = fuzz.trimf(MudancaDeTensao.universe, [108, 130, 152])
MudancaDeTensao["PG"] = fuzz.trimf(MudancaDeTensao.universe, [130, 152, 174])
MudancaDeTensao["+/-G"] = fuzz.trimf(MudancaDeTensao.universe, [152, 174, 196])
MudancaDeTensao["MG"] = fuzz.trimf(MudancaDeTensao.universe, [174, 196, 218])
MudancaDeTensao["MMG"] = fuzz.trimf(MudancaDeTensao.universe, [196, 218, 240])
MudancaDeTensao["MX"] = fuzz.trapmf(MudancaDeTensao.universe, [218, 240, 250, 250])

r1 = control.Rule(
    (MudancaDeVelocidade["MI"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["MI"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["MME"] & TensaoInicial["MP"])
    | (MudancaDeVelocidade["MME"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["MME"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["PG"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["MMG"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["MX"]),
    MudancaDeTensao["MI"],
)
r2 = control.Rule(
    (MudancaDeVelocidade["MI"] & TensaoInicial["MP"])
    | (MudancaDeVelocidade["MI"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["MI"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["MI"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["MME"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["MME"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["MME"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["MME"] & TensaoInicial["PG"])
    | (MudancaDeVelocidade["MME"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["MME"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["MP"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["MMG"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["PG"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["MMG"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["PG"] & TensaoInicial["MX"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["MX"]),
    MudancaDeTensao["MME"],
)
r3 = control.Rule(
    (MudancaDeVelocidade["MI"] & TensaoInicial["PG"])
    | (MudancaDeVelocidade["MI"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["MME"] & TensaoInicial["MMG"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["PG"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["MMG"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["MX"])
    | (MudancaDeVelocidade["MMG"] & TensaoInicial["MX"]),
    MudancaDeTensao["MP"],
)
r4 = control.Rule(
    (MudancaDeVelocidade["MI"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["MP"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["MP"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["MX"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["PG"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["PG"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["PG"] & TensaoInicial["MMG"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["MMG"])
    | (MudancaDeVelocidade["MX"] & TensaoInicial["MX"]),
    MudancaDeTensao["+/-P"],
)
r5 = control.Rule(
    (MudancaDeVelocidade["MI"] & TensaoInicial["MMG"])
    | (MudancaDeVelocidade["+/-P"] & TensaoInicial["MX"])
    | (MudancaDeVelocidade["PP"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["MP"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["PG"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["PG"] & TensaoInicial["PG"])
    | (MudancaDeVelocidade["PG"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["MMG"]),
    MudancaDeTensao["PP"],
)
r6 = control.Rule(
    (MudancaDeVelocidade["MME"] & TensaoInicial["MX"])
    | (MudancaDeVelocidade["MP"] & TensaoInicial["MX"])
    | (MudancaDeVelocidade["ME"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["PG"] & TensaoInicial["MP"])
    | (MudancaDeVelocidade["PG"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["PG"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["PG"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["MMG"] & TensaoInicial["MMG"]),
    MudancaDeTensao["ME"],
)
r7 = control.Rule(
    (MudancaDeVelocidade["PG"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["PG"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["MP"])
    | (MudancaDeVelocidade["+/-G"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["MMG"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["MMG"] & TensaoInicial["MG"])
    | (MudancaDeVelocidade["MX"] & TensaoInicial["MMG"]),
    MudancaDeTensao["PG"],
)
r8 = control.Rule(
    (MudancaDeVelocidade["MI"] & TensaoInicial["MX"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["MG"] & TensaoInicial["MP"])
    | (MudancaDeVelocidade["MMG"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["MMG"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["MMG"] & TensaoInicial["PG"])
    | (MudancaDeVelocidade["MX"] & TensaoInicial["+/-G"])
    | (MudancaDeVelocidade["MX"] & TensaoInicial["MG"]),
    MudancaDeTensao["+/-G"],
)
r9 = control.Rule(
    (MudancaDeVelocidade["MMG"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["MMG"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["MMG"] & TensaoInicial["MP"])
    | (MudancaDeVelocidade["MMG"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["MX"] & TensaoInicial["+/-P"])
    | (MudancaDeVelocidade["MX"] & TensaoInicial["PP"])
    | (MudancaDeVelocidade["MX"] & TensaoInicial["ME"])
    | (MudancaDeVelocidade["MX"] & TensaoInicial["PG"]),
    MudancaDeTensao["MG"],
)
r10 = control.Rule(
    (MudancaDeVelocidade["MX"] & TensaoInicial["MI"])
    | (MudancaDeVelocidade["MX"] & TensaoInicial["MME"])
    | (MudancaDeVelocidade["MX"] & TensaoInicial["MP"]),
    MudancaDeTensao["MMG"],
)

tensao_controle = control.ControlSystem([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10])

motor = control.ControlSystemSimulation(tensao_controle)

motor.input["MudancaDeVelocidade"] = 30
motor.input["TensaoInicial"] = 65

motor.compute()
print(motor.output)

MudancaDeTensao.view(sim=motor)