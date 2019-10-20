from functools import partial


def job(in_hour_money, work):   # in_hour_money = ставка в час work = выработка в часах
    def job_prem(prem):
        return (in_hour_money * work + prem)
    return job_prem

main_job = partial(job, 100, 8)()
print(main_job(100))
