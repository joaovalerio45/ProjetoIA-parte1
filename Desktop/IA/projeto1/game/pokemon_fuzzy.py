import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

'''
Cria um sistema Fuzzy que recebe como input a diferença dos niveis
e o efeito do ataque e devolve como input a probabilidade de ganhar
'''

level_diff = ctrl.Antecedent(np.arange(-10, 11, 1), 'level_diff')
effect = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'effect')
prob = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'prob')


level_diff['negative'] = fuzz.trapmf(level_diff.universe, [-10, -10, -2, 0])
level_diff['zero'] = fuzz.trimf(level_diff.universe, [-2, 0, 2])
level_diff['positive'] = fuzz.trapmf(level_diff.universe, [0, 2, 10, 10])

effect['weak'] = fuzz.trapmf(effect.universe, [0, 0, 0.25, 1])
effect['normal'] = fuzz.trimf(effect.universe, [0.5, 1, 2])
effect['strong'] = fuzz.trapmf(effect.universe, [1, 2, 4, 4])

prob['low'] = fuzz.trapmf(prob.universe, [0, 0, 0.3, 0.5])
prob['medium'] = fuzz.trimf(prob.universe, [0.3, 0.5, 0.7])
prob['high'] = fuzz.trapmf(prob.universe, [0.5, 0.7, 1, 1])


rule1 = ctrl.Rule(level_diff['negative'] & effect['weak'], prob['low'])
rule2 = ctrl.Rule(level_diff['negative'] & effect['normal'], prob['low'])
rule3 = ctrl.Rule(level_diff['negative'] & effect['strong'], prob['medium'])

rule4 = ctrl.Rule(level_diff['zero'] & effect['weak'], prob['low'])
rule5 = ctrl.Rule(level_diff['zero'] & effect['normal'], prob['medium'])
rule6 = ctrl.Rule(level_diff['zero'] & effect['strong'], prob['high'])

rule7 = ctrl.Rule(level_diff['positive'] & effect['weak'], prob['medium'])
rule8 = ctrl.Rule(level_diff['positive'] & effect['normal'], prob['high'])
rule9 = ctrl.Rule(level_diff['positive'] & effect['strong'], prob['high'])


prob_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, 
    rule4, rule5, rule6, 
    rule7, rule8, rule9
])
prob_sim = ctrl.ControlSystemSimulation(prob_ctrl)

def calculate_prob(level_input, effect_input):
    level_input = max(min(level_input, 10), -10)
    effect_input = max(min(effect_input, 4.0), 0.0)
    
    prob_sim.input['level_diff'] = float(level_input)
    prob_sim.input['effect'] = float(effect_input)
    
    try:
        prob_sim.compute()
        return prob_sim.output['prob']
    except ValueError:
        return 0.0
    


