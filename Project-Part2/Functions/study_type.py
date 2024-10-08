def type_study (common_sr, common_os, common_ma, common_rct):
    len_sr = len(common_sr)
    len_os = len(common_os)
    len_ma = len(common_ma)
    len_rct = len(common_rct)
    len_list = [len_os, len_rct, len_sr, len_ma]  # from less evidence to more evidence
    type_paper = ['observational study', 'randomised control trials', 'systematic review',
                  'meta analysis']  # same order

    m = max(len_list)
    if m == 0:
        return 'other'
    elif m !=0:
        MAX = [i for i, j in enumerate(len_list) if j == m]
        TYPE = type_paper[MAX[-1]]
        return TYPE