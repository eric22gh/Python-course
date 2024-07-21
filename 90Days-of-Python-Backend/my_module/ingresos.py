def calculo_ingresos(ventas, donaciones):
    ingreso = ventas + donaciones
    return f"Este es el resultado del calculo de los ingresos totales: {ingreso} colones"
calculo_ingresos(200000, 50000)