import matplotlib.pyplot as plt
from ipywidgets import  widgets

def waermeleitung(lambda_b, lambda_p, d_b,  d_p):
    T_i = 20
    T_a = -10
    
    delta_Tp = round((T_i-T_a)/(1+(lambda_p*d_b)/(lambda_b*d_p)),1)
    T_ue = round(delta_Tp + T_a,2)


    fig, ax = plt.subplots(figsize=(7.5, 5))
    ax.set_xlim([-10, 45])
    ax.set_ylim([-15, 25])
    ax.set_xlabel("x-Position in $cm$")
    ax.set_ylabel("Temperatur in $°C$")
    
    # Beton
    t1 = plt.Polygon([[0,-15],[0,25],[d_b,25],[d_b,-15]],  hatch='\\', alpha = 0.5)
    plt.gca().add_patch(t1)
    # Poly
    t2 = plt.Polygon([[d_b,-15],[d_b,25],[d_p+d_b,25],[d_p+d_b,-15]], hatch='.',alpha = 0.3)
    plt.gca().add_patch(t2)

    ax.scatter(0, 20, s=50, color="r", zorder = 2)
    ax.scatter(d_p+d_b, -10, s=50, color="r", zorder = 2)
    ax.scatter(d_b, T_ue, s=50, color="r", zorder = 2)

    plt.plot([0, d_b], [20, T_ue], color="r")
    plt.plot([d_b, d_p + d_b], [T_ue, -10], color="r")

    ta_t = plt.text(-5, 20, r'$T_{innen}$', fontsize=12)
    ti_t = plt.text(d_p + d_b+1, -10, r'$T_{außen}$', fontsize=12)
    tu_t = plt.text(d_b, T_ue, r'$T_{ü}$', fontsize=12)
    return plt.show()

lambda_b = widgets.FloatSlider(value=2.5, min=1, max=3,step=0.1,description=r'$\lambda_{Beton} \, [W K⁻¹m⁻¹]$', style={'description_width': 'initial'}, continuous_update=False)
d_b = widgets.FloatSlider(value=15, min=0.001, max=20.5,step=0.5,description=r'$d_{Beton} \, [cm]$', style={'description_width': 'initial'}, continuous_update=False)
lambda_p = widgets.FloatSlider(value=0.03, min=0.001, max=1.5,step=0.01,description=r'$\lambda_{Poly} \, [W K⁻¹m⁻¹]$', style={'description_width': 'initial'}, continuous_update=False)
d_p = widgets.FloatSlider(value=10, min=0.001, max=20.5,step=0.5,description=r'$d_{Poly} \, [cm]$', style={'description_width': 'initial'}, continuous_update=False)