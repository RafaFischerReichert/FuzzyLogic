from time import sleep
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control

dom_velocidade = np.arange(-10, 141, 1)
dom_tensao = np.arange(-10, 251, 1)

TensaoInicial = control.Antecedent(dom_tensao, "TensaoInicial")
VelocidadeAlvo = control.Antecedent(dom_velocidade, "VelocidadeAlvo")

MudancaDeTensao = control.Consequent(dom_tensao, "MudancaDeTensao")

VelocidadeAlvo["MI"] = fuzz.trapmf(VelocidadeAlvo.universe, [-10, -10, 0, 13])
VelocidadeAlvo["MME"] = fuzz.trimf(VelocidadeAlvo.universe, [0, 13, 26])
VelocidadeAlvo["MP"] = fuzz.trimf(VelocidadeAlvo.universe, [13, 26, 39])
VelocidadeAlvo["+/-P"] = fuzz.trimf(VelocidadeAlvo.universe, [29, 39, 52])
VelocidadeAlvo["PP"] = fuzz.trimf(VelocidadeAlvo.universe, [39, 52, 65])
VelocidadeAlvo["ME"] = fuzz.trimf(VelocidadeAlvo.universe, [52, 65, 78])
VelocidadeAlvo["PG"] = fuzz.trimf(VelocidadeAlvo.universe, [65, 78, 91])
VelocidadeAlvo["+/-G"] = fuzz.trimf(VelocidadeAlvo.universe, [78, 91, 104])
VelocidadeAlvo["MG"] = fuzz.trimf(VelocidadeAlvo.universe, [91, 104, 117])
VelocidadeAlvo["MMG"] = fuzz.trimf(VelocidadeAlvo.universe, [104, 117, 130])
VelocidadeAlvo["MX"] = fuzz.trapmf(
    VelocidadeAlvo.universe, [117, 130, 140, 140]
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
    (VelocidadeAlvo["MI"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["MI"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["MME"] & TensaoInicial["MP"])
    | (VelocidadeAlvo["MME"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["MME"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["PG"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["MMG"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["MX"]),
    MudancaDeTensao["MI"],
)
r2 = control.Rule(
    (VelocidadeAlvo["MI"] & TensaoInicial["MP"])
    | (VelocidadeAlvo["MI"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["MI"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["MI"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["MME"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["MME"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["MME"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["MME"] & TensaoInicial["PG"])
    | (VelocidadeAlvo["MME"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["MME"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["MP"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["MMG"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["PG"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["MMG"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["PG"] & TensaoInicial["MX"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["MX"]),
    MudancaDeTensao["MME"],
)
r3 = control.Rule(
    (VelocidadeAlvo["MI"] & TensaoInicial["PG"])
    | (VelocidadeAlvo["MI"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["MME"] & TensaoInicial["MMG"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["PG"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["MMG"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["MX"])
    | (VelocidadeAlvo["MMG"] & TensaoInicial["MX"]),
    MudancaDeTensao["MP"],
)
r4 = control.Rule(
    (VelocidadeAlvo["MI"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["MP"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["MP"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["MX"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["PG"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["PG"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["PG"] & TensaoInicial["MMG"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["MMG"])
    | (VelocidadeAlvo["MX"] & TensaoInicial["MX"]),
    MudancaDeTensao["+/-P"],
)
r5 = control.Rule(
    (VelocidadeAlvo["MI"] & TensaoInicial["MMG"])
    | (VelocidadeAlvo["+/-P"] & TensaoInicial["MX"])
    | (VelocidadeAlvo["PP"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["MP"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["PG"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["PG"] & TensaoInicial["PG"])
    | (VelocidadeAlvo["PG"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["MMG"]),
    MudancaDeTensao["PP"],
)
r6 = control.Rule(
    (VelocidadeAlvo["MME"] & TensaoInicial["MX"])
    | (VelocidadeAlvo["MP"] & TensaoInicial["MX"])
    | (VelocidadeAlvo["ME"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["PG"] & TensaoInicial["MP"])
    | (VelocidadeAlvo["PG"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["PG"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["PG"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["MMG"] & TensaoInicial["MMG"]),
    MudancaDeTensao["ME"],
)
r7 = control.Rule(
    (VelocidadeAlvo["PG"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["PG"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["MP"])
    | (VelocidadeAlvo["+/-G"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["MMG"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["MMG"] & TensaoInicial["MG"])
    | (VelocidadeAlvo["MX"] & TensaoInicial["MMG"]),
    MudancaDeTensao["PG"],
)
r8 = control.Rule(
    (VelocidadeAlvo["MI"] & TensaoInicial["MX"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["MG"] & TensaoInicial["MP"])
    | (VelocidadeAlvo["MMG"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["MMG"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["MMG"] & TensaoInicial["PG"])
    | (VelocidadeAlvo["MX"] & TensaoInicial["+/-G"])
    | (VelocidadeAlvo["MX"] & TensaoInicial["MG"]),
    MudancaDeTensao["+/-G"],
)
r9 = control.Rule(
    (VelocidadeAlvo["MMG"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["MMG"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["MMG"] & TensaoInicial["MP"])
    | (VelocidadeAlvo["MMG"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["MX"] & TensaoInicial["+/-P"])
    | (VelocidadeAlvo["MX"] & TensaoInicial["PP"])
    | (VelocidadeAlvo["MX"] & TensaoInicial["ME"])
    | (VelocidadeAlvo["MX"] & TensaoInicial["PG"]),
    MudancaDeTensao["MG"],
)
r10 = control.Rule(
    (VelocidadeAlvo["MX"] & TensaoInicial["MI"])
    | (VelocidadeAlvo["MX"] & TensaoInicial["MME"])
    | (VelocidadeAlvo["MX"] & TensaoInicial["MP"]),
    MudancaDeTensao["MMG"],
)

tensao_controle = control.ControlSystem([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10])

motor_a = control.ControlSystemSimulation(tensao_controle)
motor_a.input["VelocidadeAlvo"] = 30
motor_a.input["TensaoInicial"] = 65
motor_a.compute()
MudancaDeTensao.view(sim=motor_a)
print(motor_a.output)

motor_b = control.ControlSystemSimulation(tensao_controle)
motor_b.input["VelocidadeAlvo"] = 110
motor_b.input["TensaoInicial"] = 80
motor_b.compute()
MudancaDeTensao.view(sim=motor_b)
print(motor_b.output)

motor_c = control.ControlSystemSimulation(tensao_controle)
motor_c.input["VelocidadeAlvo"] = 40
motor_c.input["TensaoInicial"] = 0
motor_c.compute()
MudancaDeTensao.view(sim=motor_c)
print(motor_c.output)