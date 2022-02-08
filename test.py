import os, sys
try:sys.path.insert(0, os.path.dirname(__file__)+'/codes3/')
except:sys.path.insert(0, 'D:/DrH/Codes/acmop/codes3/')
finally:import acmop

mop = acmop.AC_Machine_Optiomization_Wrapper(
    # select_spec='IM Q24p1y9 Qr32 Round Bar',
    # select_fea_config_dict = '#019 JMAG IM Nine Variables',

    select_spec            = 'PMSM Q12p4y1 A', #'PMSM Q18p4y2 Beijing ShiDaiChaoQun',
    # select_fea_config_dict = '#02 JMAG PMSM Evaluation Setting',
    select_fea_config_dict = '#04 FEMM PMSM Evaluation Setting',

    project_loc            = fr'D:/DrH/Codebs/acmop/_default/',
    bool_show_GUI          = True
)

# quit()

#########################
# Call the five modules
#########################
# mop.part_winding() # Module 1
# mop.acm_template # Module 2 (the execution code has been moved to the end of __post_init__ of AC_Machine_Optiomization_Wrapper)
if True:
    mop.part_evaluation() # Module 3
    # mop.part_optimization(acm_template) # Module 4
else:
    if True:
        motor_design_variant = mop.reproduce_design_from_jsonpickle('p4ps5-Q12y1-0999') # Module 5 - reproduction of any design variant object
    else:
        mop.part_post_optimization_analysis(project_name='proj12-SPMSM_IDQ12p4s1') # Module 5 - visualize swarm data
        # mop.part_post_optimization_analysis(project_name='proj212-SPMSM_IDQ12p1s1') # Module 5




''' Interactive variable checking example:
>>> GP = mop.ad.acm_variant.template.d['GP'] 
>>> GP['mm_r_ri'].value + GP['mm_d_ri'].value + GP['mm_d_rp'].value 
46.7464829275686
>>> GP['mm_r_or'] 
acmop_parameter(type='derived', name='outer_rotor_radius', value=47.7464829275686, bounds=[None, None], calc=<function template_machine_as_numbers.__init__.<locals>.<lambda> at 0x00000130CF961790>)
'''