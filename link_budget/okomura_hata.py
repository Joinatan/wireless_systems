import numpy as np

def okomura_hata(h_t, h_r, d, f, city_type = 'medium'):
    #COST 231
    if(f > 1500):
        loss = 46.3 + 33.9 * np.log10(f) - 13.82 * np.log10(h_t) + (44.9 - 6.55 * np.log10(h_t)) * np.log10(d)
        if(city_type == 'large'):
            loss = loss + 3
    else:
        loss = 69.55 + 26 * np.log10(f) - 13.82 * np.log10(h_t) + (44.9 - 6.55 * np.log10(h_t)) * np.log10(d)

    match city_type:
        case 'medium':
            A = (1.1 * np.log10(f) - 0.7) * h_r - (1.56 * np.log10(f) - 0.8)
            return loss - A
        case 'large':
            if(f < 300):
                A = 8.29 * (np.log10(1.54 * h_r))**2 - 1.1
                return loss - A
            else:
                A = 3.2 * (np.log10(11.75 * h_r))**2 - 4.97
                print(A)
                print(loss)
                print('hej')
                return loss - A
        case 'suburban':
            #A equals medium city here
            A = (1.1 * np.log10(f) - 0.7) * h_r - (1.56 * np.log10(f) - 0.8)
            return (loss - A) - 2 * (np.log10(f/28))**2 - 5.4
        case 'rural':
            #A equals medium city here
            A = (1.1 * np.log10(f) - 0.7) * h_r - (1.56 * np.log10(f) - 0.8)
            return (loss - A) - 4.78 * (np.log10(f))**2 - 18.733 * np.log10(f) - 40.98
        case _:
            return "no valid city"
