from mvc import Controller
# import mvc

# controller = mvc.Controller()
controller = Controller()

# Displaying Summary for defect id # 2
print(controller.get_defect_summary(2))

# Displaying defect list for 'ABC' Component
print(controller.get_defect_list('ABC'))
