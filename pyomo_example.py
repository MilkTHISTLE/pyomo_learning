from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory, NonNegativeReals, maximize

# 모델 생성
model = ConcreteModel()

# 변수 추가
model.x = Var(domain=NonNegativeReals)
model.y = Var(domain=NonNegativeReals)

# 목적 함수 설정
model.obj = Objective(expr=2 * model.x + 3 * model.y, sense=maximize)

# 제약 조건 추가
model.con1 = Constraint(expr=model.x + model.y <= 4)
model.con2 = Constraint(expr=model.x - model.y >= 1)

# 솔버 설정 및 최적화 수행
solver = SolverFactory('glpk')
solver.solve(model)

# 결과 출력
print(f'x = {model.x()}, y = {model.y()}')
print(f'Objective value: {model.obj()}')
