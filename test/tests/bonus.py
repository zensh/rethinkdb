from lib.framework import TestTree
from scenarios.more_or_less_secondaries import MoreOrLessSecondaries
from workloads.stress import Stress

# TODO

tests = TestTree()

def heavy_backfilling():
    MoreOrLessSecondaries(
        [1, +1],
        workload_during = Stress(
            operations={'inserts':1},
            duration='infinity',
            qps_out='qps_out'),
        extra_before=200)


# TODO
# # Test repeatedly reconfiguring the server while also running HTTP queries against it
# generate_test(
#     "$RETHINKDB/test/scenarios/more_or_less_secondaries.py 2+1-1+1-1+1-1+1-1+1-1 "
#         "--workload-before '$RETHINKDB/test/memcached_workloads/serial_mix.py $HOST:$PORT --save x' "
#         "--workload-between '$RETHINKDB/test/memcached_workloads/serial_mix.py $HOST:$PORT --load x --save x' "
#         "--workload-after '$RETHINKDB/test/memcached_workloads/serial_mix.py $HOST:$PORT --load x' "
#         "--workload-during '$RETHINKDB/test/memcached_workloads/simulate_web_ui.py $HOST:$HTTP_PORT'",
#         name = "reconfigure-under-load-1"
#     )

# generate_test(
#     "$RETHINKDB/test/scenarios/more_or_less_secondaries.py 2+1-1+1-1+1-1+1-1+1-1 "
#         "--workload-during '$RETHINKDB/bench/stress-client/stress -s sockmemcached,$HOST:$PORT -w 0/0/1/0 -d infinity -q qps_out' "
#         "--workload-during '$RETHINKDB/test/memcached_workloads/simulate_web_ui.py $HOST:$HTTP_PORT'",
#         name = "reconfigure-under-load-2"
#     )

# generate_test(
#     "$RETHINKDB/test/scenarios/rebalance.py --sequence 0,++++++++,----,++++++++,------------ "
#         "--workload-before '$RETHINKDB/bench/stress-client/stress -s sockmemcached,$HOST:$PORT -w 0/0/1/0 -d 10s -o keys.out' "
#         "--workload-during '$RETHINKDB/bench/stress-client/stress -s sockmemcached,$HOST:$PORT -w 0/0/1/0 -d infinity -q qps_out -i keys.out --ignore-protocol-errors' "
#         "--workload-during '$RETHINKDB/test/memcached_workloads/simulate_web_ui.py $HOST:$HTTP_PORT' "
#         "--workload-after '$RETHINKDB/bench/stress-client/stress -s sockmemcached,$HOST:$PORT -d 10s -i keys.out'",
#         name = "reconfigure-under-load-3"
#     )
