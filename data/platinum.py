from util.locations import Category, Location, Entrance

INITIAL_LOCATION = Category('sandgem_jubilife', 'Sandgem/Jubilife', [])

CATEGORIES = [
    Category('poi', 'Places of Interest', [
        Location('oreburgh_gym_interior', 'Oreburgh Gym Interior',
                 [Entrance('oreburgh_gym_interior', 'Oreburgh Gym Interior')]),
        Location('eterna_gym_interior', 'Eterna Gym Interior',
                 [Entrance('eterna_gym_interior', 'Eterna Gym Interior')]),
        Location('hearthome_gym_interior', 'Hearthome Gym Interior',
                 [Entrance('hearthome_gym_interior', 'Hearthome Gym Interior')]),
        Location('veilstone_gym_interior', 'Veilstone Gym Interior',
                 [Entrance('veilstone_gym_interior', 'Veilstone Gym Interior')]),
        Location('pastoria_gym_interior', 'Pastoria Gym Interior',
                 [Entrance('pastoria_gym_interior', 'Pastoria Gym Interior')]),
        Location('canalave_gym_interior', 'Canalave Gym Interior',
                 [Entrance('canalave_gym_interior', 'Canalave Gym Interior')]),
        Location('snowpoint_gym_interior', 'Snowpoint Gym Interior',
                 [Entrance('snowpoint_gym_interior', 'Snowpoint Gym Interior')]),
        Location('sunyshore_gym_interior', 'Sunyshore Gym Interior',
                 [Entrance('sunyshore_gym_interior', 'Sunyshore Gym Interior')]),
        Location('e4_aaron', 'E4 Aaron',
                 [Entrance('e4_aaron', 'E4 Aaron')]),
        Location('e4_bertha', 'E4 Bertha',
                 [Entrance('e4_bertha', 'E4 Bertha')]),
        Location('e4_flint', 'E4 Flint',
                 [Entrance('e4_flint', 'E4 Flint')]),
        Location('e4_lucian', 'E4 Lucian',
                 [Entrance('e4_lucian', 'E4 Lucian')]),
        Location('champion', 'Champion',
                 [Entrance('champion', 'Champion')]),
        Location('dialga_palkia', 'Dialga/Palkia',
                 [Entrance('dialga_palkia', 'Dialga/Palkia')]),
        Location('cresselia', 'Cresselia',
                 [Entrance('cresselia', 'Cresselia')]),
        Location('darkrai', 'Darkrai',
                 [Entrance('darkrai', 'Darkrai')]),
        Location('heatran', 'Heatran',
                 [Entrance('heatran', 'Heatran')]),
        Location('arceus', 'Arceus',
                 [Entrance('arceus', 'Arceus')]),
        Location('azelf', 'Azelf',
                 [Entrance('azelf', 'Azelf')]),
        Location('uxie', 'Uxie',
                 [Entrance('uxie', 'Uxie')]),
    ]),
    Category('sandgem_jubilife', 'Sandgem/Jubilife', [
        Location('sandgem_pc', 'Sandgem PC', [
            Entrance('sandgem_pc_w', 'Sandgem PC W'),
            Entrance('sandgem_pc_s', 'Sandgem PC S'),
            Entrance('sandgem_pc_e', 'Sandgem PC E'),
        ]),
        Location('jubilife_pc', 'Jubilife PC', [
            Entrance('jubilife_pc_w', 'Jubilife PC W'),
            Entrance('jubilife_pc_s', 'Jubilife PC S'),
            Entrance('jubilife_pc_e', 'Jubilife PC E'),
        ]),
        Location('sandgem_jubilife', 'Sandgem/Jubilife', [
            Entrance('verity_lakefront', 'Verity Lakefront'),
            Entrance('sandgem_pokecenter', 'Sandgem Pokécenter'),
            Entrance('sandgem_mart', 'Sandgem Mart'),
            Entrance('sandgem_sw', 'Sandgem SW'),
            Entrance('sandgem_s', 'Sandgem S'),
            Entrance('jubilife_pokecenter', 'Jubilife Pokécenter'),
            Entrance('jubilife_mart', 'Jubilife Mart'),
            Entrance('jubilife_s', 'Jubilife S'),
            Entrance('jubilife_sw', 'Jubilife SW'),
            Entrance('jubilife_ne', 'Jubilife NE'),
            Entrance('jubilife_gts', 'Jubilife GTS'),
            Entrance('jubilife_tv', 'Jubilife TV'),
            Entrance('jubilife_poketch_w', 'Jubilife Poketch W'),
            Entrance('jubilife_poketch_e', 'Jubilife Poketch E'),
            Entrance('jubilife_ravaged_path', 'Jubilife Ravaged Path'),
            Entrance('jubilife_oreburgh_gate', 'Jubilife Oreburgh Gate'),
            Entrance('jubilife_west_exit', 'Jubilife West Exit'),
        ]),
    ]),
    Category('oreburgh', 'Oreburgh', [
        Location('oreburgh_pc', 'Oreburgh PC', [
            Entrance('oreburgh_pc_w', 'Oreburgh PC W'),
            Entrance('oreburgh_pc_s', 'Oreburgh PC S'),
            Entrance('oreburgh_pc_e', 'Oreburgh PC E'),
        ]),
        Location('oreburgh', 'Oreburgh', [
            Entrance('oreburgh_pokecenter', 'Oreburgh Pokécenter'),
            Entrance('oreburgh_mart', 'Oreburgh Mart'),
            Entrance('oreburgh_gym', 'Oreburgh Gym'),
            Entrance('oreburgh_fossil_lab', 'Oreburgh Fossil Lab'),
            Entrance('oreburgh_mine', 'Oreburgh Mine'),
            Entrance('oreburgh_apartment_nw', 'Oreburgh Apartment NW'),
            Entrance('oreburgh_apartment_n', 'Oreburgh Apartment N'),
            Entrance('oreburgh_apartment_e', 'Oreburgh Apartment E'),
            Entrance('oreburgh_house_w', 'Oreburgh House W'),
            Entrance('oreburgh_house_c', 'Oreburgh House C'),
            Entrance('oreburgh_house_se', 'Oreburgh House SE'),
            Entrance('oreburgh_west_exit', 'Oreburgh West Exit'),
            Entrance('r206_cycle_path', 'R206 Cycle Path'),
            Entrance('r206_wayward_cave', 'R206 Wayward Cave'),
            Entrance('r206_wayward_cave_hidden', 'R206 Wayward Cave Hidden'),
            Entrance('r207_mt_coronet', 'R207 Mt Coronet'),
        ]),
    ]),
    Category('floaroma', 'Floaroma', [
        Location('floaroma_pc', 'Floaroma PC', [
            Entrance('floaroma_pc_w', 'Floaroma PC W'),
            Entrance('floaroma_pc_s', 'Floaroma PC S'),
            Entrance('floaroma_pc_e', 'Floaroma PC E'),
        ]),
        Location('floaroma', 'Floaroma', [
            Entrance('floaroma_pokecenter', 'Floaroma Pokecenter'),
            Entrance('floaroma_mart', 'Floaroma Mart'),
            Entrance('floaroma_flower_shop', 'Floaroma Flower Shop'),
            Entrance('floaroma_nw', 'Floaroma NW'),
            Entrance('floaroma_se', 'Floaroma SE'),
            Entrance('floaroma_ravaged_path', 'Floaroma Ravaged Path'),
            Entrance('floaroma_meadow_entrance_floaroma', 'Meadow Entrance Floaroma'),
            Entrance('r205_ironworks', 'R205 Ironworks'),
            Entrance('floaroma_meadow_entrance_iron', 'R205 Meadow Entrance'),
            Entrance('r205_windworks', 'R205 Windworks'),
            Entrance('r205_eterna_forest', 'R205 Eterna Forest'),
            Entrance('r205_house', 'R205 House'),
        ]),
        Location('meadow', 'Floaroma Meadow', [
            Entrance('floaroma_meadow_exit_house', 'Meadow House'),
            Entrance('floaroma_meadow_exit_n', 'Meadow Exit N'),
            Entrance('floaroma_meadow_exit_s', 'Meadow Exit S'),
        ]),
    ]),
    Category('eterna', 'Eterna', [
        Location('eterna_pc', 'Eterna PC', [
            Entrance('eterna_pc_w', 'Eterna PC W'),
            Entrance('eterna_pc_s', 'Eterna PC S'),
            Entrance('eterna_pc_e', 'Eterna PC E'),
        ]),
        Location('eterna', 'Eterna', [
            Entrance('eterna_pokecenter', 'Eterna Pokecenter'),
            Entrance('eterna_mart', 'Eterna Mart'),
            Entrance('eterna_gym', 'Eterna Gym'),
            Entrance('eterna_bike_shop', 'Eterna Bike Shop'),
            Entrance('eterna_spelunkers_house', 'Spelunker\'s House'),
            Entrance('eterna_city_forest', 'Eterna City Forest'),
            Entrance('eterna_apartment', 'Eterna Apartment'),
            Entrance('eterna_galactic', 'Eterna Galactic Building'),
            Entrance('eterna_house_n', 'Eterna House N'),
            Entrance('eterna_house_s', 'Eterna House S'),
            Entrance('eterna_house_e', 'Eterna House E'),
            Entrance('eterna_mt_coronet', 'Eterna Mt Coronet'),
            Entrance('eterna_south_exit', 'Eterna South Exit'),
        ]),
    ]),
    Category('hearthome', 'Hearthome', [
        Location('hearthome_pc', 'Hearthome PC', [
            Entrance('hearthome_pc_w', 'Hearthome PC W'),
            Entrance('hearthome_pc_s', 'Hearthome PC S'),
            Entrance('hearthome_pc_e', 'Hearthome PC E'),
        ]),
        Location('hearthome', 'Hearthome', [
            Entrance('hearthome_pokecenter', 'Hearthome Pokecenter'),
            Entrance('hearthome_mart', 'Hearthome Mart'),
            Entrance('hearthome_gym', 'Hearthome Gym'),
            Entrance('hearthome_contest', 'Hearthome Contest'),
            Entrance('hearthome_bebes_house', 'Bebe\'s house'),
            Entrance('hearthome_church', 'Hearthome Church'),
            Entrance('hearthome_poffin_house', 'Hearthome Poffin House'),
            Entrance('hearthome_fanclub', 'Hearthome Fanclub'),
            Entrance('hearthome_apartment_n', 'Hearthome Apartment N'),
            Entrance('hearthome_apartment_e', 'Hearthome Apartment E'),
            Entrance('hearthome_amity_square_west', 'Amity Square West'),
            Entrance('hearthome_amity_square_east', 'Amity Square East'),
            Entrance('hearthome_east_exit', 'Hearthome East Exit'),
            Entrance('hearthome_south_exit', 'Hearthome South Exit'),
            Entrance('hearthome_west_exit', 'Hearthome West Exit'),
        ]),
    ]),
    Category('solaceon', 'Solaceon', [
        Location('solaceon_pc', 'Solaceon PC', [
            Entrance('solaceon_pc_w', 'Solaceon PC W'),
            Entrance('solaceon_pc_s', 'Solaceon PC S'),
            Entrance('solaceon_pc_e', 'Solaceon PC E'),
        ]),
        Location('solaceon', 'Solaceon', [
            Entrance('solaceon_pokecenter', 'Solaceon Pokecenter'),
            Entrance('solaceon_mart', 'Solaceon Mart'),
            Entrance('solaceon_daycare', 'Solaceon Daycare'),
            Entrance('solaceon_house_n', 'Solaceon House N'),
            Entrance('solaceon_house_ne', 'Solaceon House NE'),
            Entrance('solaceon_house_e', 'Solaceon House E'),
            Entrance('solaceon_house_c', 'Solaceon House C'),
            Entrance('solaceon_ruins', 'Solaceon Ruins'),
            Entrance('r209_lost_tower', 'R209 Lost Tower'),
            Entrance('r209_west_exit', 'R209 West Exit'),
            Entrance('r210_cafe_cabin', 'R210 Cafe Cabin'),
            Entrance('r215_east_exit', 'R215 East Exit'),
        ]),
    ]),
    Category('veilstone', 'Veilstone', [
        Location('veilstone_pc', 'Veilstone PC', [
            Entrance('veilstone_pc_w', 'Veilstone PC W'),
            Entrance('veilstone_pc_s', 'Veilstone PC S'),
            Entrance('veilstone_pc_e', 'Veilstone PC E'),
        ]),
        Location('veilstone', 'Veilstone', [
            Entrance('veilstone_pokecenter', 'Veilstone Pokecenter'),
            Entrance('veilstone_mart', 'Veilstone Mart'),
            Entrance('veilstone_gym', 'Veilstone Gym'),
            Entrance('veilstone_casino', 'Veilstone Casino'),
            Entrance('veilstone_galactic_hq_1', 'Galactic HQ 1'),
            Entrance('veilstone_galactic_hq_2', 'Galactic HQ 2'),
            Entrance('veilstone_galactic_hq_3', 'Galactic HQ 3'),
            Entrance('veilstone_galactic_warehouse', 'Galactic Warehouse'),
            Entrance('veilstone_house_n', 'Veilstone House N'),
            Entrance('veilstone_house_ne', 'Veilstone House NE'),
            Entrance('veilstone_prize_exchange', 'Prize Exchange'),
            Entrance('veilstone_house_s', 'Veilstone House S'),
            Entrance('veilstone_house_sw', 'Veilstone House SW'),
            Entrance('veilstone_south_exit', 'Veilstone South Exit'),
            Entrance('veilstone_west_exit', 'Veilstone West Exit'),
        ]),
    ]),
    Category('pastoria', 'Pastoria', [
        Location('pastoria_pc', 'Pastoria PC', [
            Entrance('pastoria_pc_w', 'Pastoria PC W'),
            Entrance('pastoria_pc_s', 'Pastoria PC S'),
            Entrance('pastoria_pc_e', 'Pastoria PC E'),
        ]),
        Location('pastoria', 'Pastoria', [
            Entrance('pastoria_pokecenter', 'Pastoria Pokecenter'),
            Entrance('pastoria_mart', 'Pastoria Mart'),
            Entrance('pastoria_gym', 'Pastoria Gym'),
            Entrance('pastoria_house_ne', 'Pastoria House NE'),
            Entrance('pastoria_house_se', 'Pastoria House SE'),
            Entrance('pastoria_house_sw', 'Pastoria House SW'),
            Entrance('pastoria_house_n', 'Pastoria House N'),
            Entrance('pastoria_house_c', 'Pastoria House C'),
            Entrance('pastoria_east_exit', 'Pastoria East Exit'),
            Entrance('r212_move_tutor', 'R212 Move Tutor'),
            Entrance('r212_pokemon_mansion', 'R212 Pokemon Mansion'),
            Entrance('r212_north_exit', 'R212 North Exit'),
        ]),
    ]),
    Category('celestic', 'Celestic', [
        Location('celestic_pc', 'Celestic PC', [
            Entrance('celestic_pc_w', 'Celestic PC W'),
            Entrance('celestic_pc_s', 'Celestic PC S'),
            Entrance('celestic_pc_e', 'Celestic PC E'),
        ]),
        Location('celestic', 'Celestic', [
            Entrance('celestic_pokecenter', 'Celestic Pokecenter'),
            Entrance('celestic_ruins', 'Celestic Ruins'),
            Entrance('celestic_big_house', 'Celestic Big House'),
            Entrance('celestic_house_ne', 'Celestic House NE'),
            Entrance('celestic_house_nw', 'Celestic House NW'),
            Entrance('celestic_house_sw', 'Celestic House SW'),
            Entrance('celestic_mt_coronet', 'Celestic Mt Coronet'),
            Entrance('r210_grandmas_house', 'R210 Grandmas House'),
        ]),
    ]),
    Category('canalave', 'Canalave', [
        Location('canalave_pc', 'Canalave PC', [
            Entrance('canalave_pc_w', 'Canalave PC W'),
            Entrance('canalave_pc_s', 'Canalave PC S'),
            Entrance('canalave_pc_e', 'Canalave PC E'),
        ]),
        Location('canalave', 'Canalave', [
            Entrance('canalave_pokecenter', 'Canalave Pokecenter'),
            Entrance('canalave_mart', 'Canalave Mart'),
            Entrance('canalave_gym', 'Canalave Gym'),
            Entrance('canalave_library', 'Canalave Library'),
            Entrance('canalave_house_e', 'Canalave House E'),
            Entrance('canalave_house_se', 'Canalave House SE'),
            Entrance('canalave_house_ne', 'Canalave House NE'),
            Entrance('canalave_house_w', 'Canalave House W'),
            Entrance('canalave_house_sw', 'Canalave House SW'),
            Entrance('canalave_east_exit', 'Canalave East Exit'),
        ]),
    ]),
    Category('snowpoint', 'Snowpoint', [
        Location('snowpoint_pc', 'Snowpoint PC', [
            Entrance('snowpoint_pc_w', 'Snowpoint PC W'),
            Entrance('snowpoint_pc_s', 'Snowpoint PC S'),
            Entrance('snowpoint_pc_e', 'Snowpoint PC E'),
        ]),
        Location('snowpoint', 'Snowpoint', [
            Entrance('snowpoint_pokecenter', 'Snowpoint Pokecenter'),
            Entrance('snowpoint_mart', 'Snowpoint Mart'),
            Entrance('snowpoint_gym', 'Snowpoint Gym'),
            Entrance('snowpoint_house_nw', 'Snowpoint House NW'),
            Entrance('snowpoint_house_ne', 'Snowpoint House NE'),
            Entrance('snowpoint_temple', 'Snowpoint Temple'),
            Entrance('acuity_lakefront', 'Acuity Lakefront'),
            Entrance('r217_house_n', 'R217 House N'),
            Entrance('r217_house_w', 'R217 House W'),
            Entrance('r216_house_w', 'R216 House W'),
            Entrance('r216_mt_coronet', 'R216 Mt Coronet'),
        ]),
    ]),
    Category('sunyshore', 'Sunyshore', [
        Location('sunyshore_pc', 'Sunyshore PC', [
            Entrance('sunyshore_pc_w', 'Sunyshore PC W'),
            Entrance('sunyshore_pc_s', 'Sunyshore PC S'),
            Entrance('sunyshore_pc_e', 'Sunyshore PC E'),
        ]),
        Location('sunyshore', 'Sunyshore', [
            Entrance('sunyshore_pokecenter', 'Sunyshore Pokecenter'),
            Entrance('sunyshore_mart', 'Sunyshore Mart'),
            Entrance('sunyshore_gym', 'Sunyshore Gym'),
            Entrance('sunyshore_lighthouse', 'Sunyshore Lighthouse'),
            Entrance('sunyshore_market', 'Sunyshore Market'),
            Entrance('sunyshore_house_w', 'Sunyshore House W'),
            Entrance('sunyshore_house_n', 'Sunyshore House N'),
            Entrance('sunyshore_house_ne', 'Sunyshore House NE'),
            Entrance('sunyshore_house_e', 'Sunyshore House E'),
            Entrance('sunyshore_west_exit', 'Sunyshore West Exit'),
        ]),
    ]),
    Category('fight_resort', 'Fight/Resort', [
        Location('fight_area_pc', 'Fight Area PC', [
            Entrance('fight_area_pc_w', 'Fight Area PC W'),
            Entrance('fight_area_pc_s', 'Fight Area PC S'),
            Entrance('fight_area_pc_e', 'Fight Area PC E'),
        ]),
        Location('resort_area_pc', 'Resort Area PC', [
            Entrance('resort_area_pc_w', 'Resort Area PC W'),
            Entrance('resort_area_pc_s', 'Resort Area PC S'),
            Entrance('resort_area_pc_e', 'Resort Area PC E'),
        ]),
        Location('fight_area', 'Fight Area', [
            Entrance('fight_area_pokecenter', 'Fight Area Pokecenter'),
            Entrance('fight_area_mart', 'Fight Area Mart'),
            Entrance('fight_area_s_house', 'Fight Area S House'),
            Entrance('fight_area_c_house', 'Fight Area C House'),
            Entrance('fight_area_north_exit', 'Fight Area North Exit'),
        ]),
        Location('resort_area', 'Resort Area', [
            Entrance('resort_area_pokecenter', 'Resort Area Pokecenter'),
            Entrance('resort_agroup-locations-together-that-you-can-reachrea_villa', 'Resort Area Villa'),
            Entrance('resort_area_ribbon_syndicate', 'Resort Area Ribbon Syndicate'),
            Entrance('resort_area_house', 'Resort Area House'),
            Entrance('r228_cave', 'R228 Cave'),
            Entrance('r228_s_house', 'R228 S House'),
            Entrance('r228_c_house', 'R228 C House'),
            Entrance('r228_north_exit', 'R228 North Exit'),
        ]),
    ]),
    Category('survival', 'Survival', [
        Location('survival_area_pc', 'Survival Area PC', [
            Entrance('survival_area_pc_w', 'Survival Area PC W'),
            Entrance('survival_area_pc_s', 'Survival Area PC S'),
            Entrance('survival_area_pc_e', 'Survival Area PC E'),
        ]),
        Location('survival', 'Survival', [
            Entrance('survival_area_pokecenter', 'Survival Area Pokecenter'),
            Entrance('survival_area_mart', 'Survival Area Mart'),
            Entrance('survival_area_n_house', 'Survival Area N House'),
            Entrance('survival_area_c_house', 'Survival Area C House'),
            Entrance('survival_area_s_house', 'Survival Area S House'),
            Entrance('r225_house', 'R225 House'),
            Entrance('r225_south_exit', 'R225 South Exit'),
            Entrance('r226_house', 'R226 House'),
            Entrance('r226_east_exit', 'R226 East Exit'),
            Entrance('r227_house', 'R227 House'),
            Entrance('r227_stark_mountain', 'R227 Stark Mountain'),
        ]),
    ]),
    Category('jubilife_tv', 'Jubilife TV', [
        Location('jubilife_tv', 'Jubilife TV', [
            Entrance('jubilife_tv_1f_up', 'TV 1F Up'),
            Entrance('jubilife_tv_1f_exit', 'TV 1F Exit'),
            Entrance('jubilife_tv_2f_n', 'TV 2F N'),
            Entrance('jubilife_tv_2f_up', 'TV 2F Up'),
            Entrance('jubilife_tv_2f_down', 'TV 2F Down'),
            Entrance('jubilife_tv_3f_nw', 'TV 3F NW'),
            Entrance('jubilife_tv_3f_n', 'TV 3F N'),
            Entrance('jubilife_tv_3f_up', 'TV 3F Up'),
            Entrance('jubilife_tv_3f_down', 'TV 3F Down'),
            Entrance('jubilife_tv_4f_down', 'TV 4F Down'),
        ]),
    ]),
    Category('store', 'Department Store', [
        Location('store', 'Department Store', [
            Entrance('store_b1f_up', 'Store B1F Up'),
            Entrance('store_1f_up', 'Store 1F Up'),
            Entrance('store_1f_down', 'Store 1F Down'),
            Entrance('store_1f_exit', 'Store 1F Exit'),
            Entrance('store_2f_up', 'Store 2F Up'),
            Entrance('store_2f_down', 'Store 2F Down'),
            Entrance('store_3f_up', 'Store 3F Up'),
            Entrance('store_3f_down', 'Store 3F Down'),
            Entrance('store_4f_up', 'Store 4F Up'),
            Entrance('store_4f_down', 'Store 4F Down'),
            Entrance('store_5f_down', 'Store 5F Down'),
        ]),
    ]),
    Category('galactic_eterna', 'Galactic Eterna', [
        Location('galactic_eterna_1f', 'Galactic Eterna 1F', [
            Entrance('galactic_eterna_1f_s', 'TG Eterna 1F Exit S'),
            Entrance('galactic_eterna_1f_nw', 'TG Eterna 1F NW'),
            Entrance('galactic_eterna_1f_stairs_n', 'TG Eterna 1F Stairs N'),
            Entrance('galactic_eterna_1f_stairs_ne', 'TG Eterna 1F Stairs NE'),
        ]),
        Location('galactic_eterna_2f', 'Galactic Eterna 2F', [
            Entrance('galactic_eterna_2f_w', 'TG Eterna 2F W'),
            Entrance('galactic_eterna_2f_n', 'TG Eterna 2F N'),
            Entrance('galactic_eterna_2f_e', 'TG Eterna 2F E'),
        ]),
        Location('galactic_eterna_3f', 'Galactic Eterna 3F', [
            Entrance('galactic_eterna_3f_w', 'TG Eterna 3F W'),
            Entrance('galactic_eterna_3f_n', 'TG Eterna 3F N'),
            Entrance('galactic_eterna_3f_e', 'TG Eterna 3F E'),
        ]),
    ]),
    Category('galactic_hq', 'Galactic HQ', [
        Location('galactic_warehouse', 'Galactic Warehouse', [
            Entrance('galactic_warehouse_b2f_stairs_c', 'Warehouse Stairs C'),
            Entrance('galactic_warehouse_b2f_stairs_e', 'Warehouse Stairs E'),
            Entrance('galactic_warehouse_b2f_stairs_w', 'Warehouse Stairs W'),
        ]),
        Location('galactic_hq_1f_a', 'Galactic HQ 1F A', [
            Entrance('galactic_hq_1f_a_stairs', 'HQ 1F A Stairs'),
            Entrance('galactic_hq_1f_a_entrance_e', 'HQ 1F A East Exit'),
            Entrance('galactic_hq_1f_a_entrance_w', 'HQ 1F A West Exit'),
        ]),
        Location('galactic_hq_1f_b', 'Galactic HQ 1F B', [
            Entrance('galactic_hq_1f_b_stairs', 'HQ 1F B Stairs'),
            Entrance('galactic_hq_1f_b_warp_e', 'HQ 1F B Warp E'),
            Entrance('galactic_hq_1f_b_warp_w', 'HQ 1F B Warp W'),
        ]),
        Location('galactic_hq_2f_a', 'Galactic HQ 2F A', [
            Entrance('galactic_hq_2f_a_stairs', 'HQ 2F A Stairs'),
            Entrance('galactic_hq_2f_a_warp_c', 'HQ 2F A Warp C'),
            Entrance('galactic_hq_2f_a_warp_ne', 'HQ 2F A Warp NE'),
            Entrance('galactic_hq_2f_a_warp_se', 'HQ 2F A Warp SE'),
        ]),
        Location('galactic_hq_2f_b', 'Galactic HQ 2F B', [
            Entrance('galactic_hq_2f_b_warp', 'HQ 2F B Warp'),
            Entrance('galactic_hq_2f_b_up', 'HQ 2F B Up'),
            Entrance('galactic_hq_2f_b_down', 'HQ 2F B Down'),
        ]),
        Location('galactic_hq_3f', 'Galactic HQ 3F', [
            Entrance('galactic_hq_3f_warp_1', 'HQ 3F Warp W'),
            Entrance('galactic_hq_3f_warp_2', 'HQ 3F Warp C'),
            Entrance('galactic_hq_3f_warp_3', 'HQ 3F Warp E'),
            Entrance('galactic_hq_3f_stairs', 'HQ 3F Stairs'),
        ]),
        Location('galactic_hq_4f', 'Galactic HQ 4F', [
            Entrance('galactic_hq_4f_stairs', 'HQ 4F Stairs'),
            Entrance('galactic_hq_4f_warp_n', 'HQ 4F Warp N'),
            Entrance('galactic_hq_4f_warp_ne', 'HQ 4F Warp NE'),
            Entrance('galactic_hq_4f_warp_se', 'HQ 4F Warp SE'),
        ]),
    ]),
    Category('pokemansion', 'Pokémansion', [
        Location('pokemansion', 'Pokémansion', [
            Entrance('poke_mansion_n', 'Pokémansion N'),
            Entrance('poke_mansion_e', 'Pokémansion E'),
            Entrance('poke_mansion_s', 'Pokémansion S'),
            Entrance('poke_mansion_w', 'Pokémansion W'),
            Entrance('poke_mansion_room_1', 'Pokémansion Room 1'),
            Entrance('poke_mansion_room_2', 'Pokémansion Room 2'),
            Entrance('poke_mansion_room_3', 'Pokémansion Room 3'),
            Entrance('poke_mansion_room_4', 'Pokémansion Room 4'),
        ]),
    ]),
    Category('old_chateau', 'Old Chateau', [
        Location('old_chateau_1f', 'Old Chateau 1F', [
            Entrance('old_chateau_n', 'OC Entrance N'),
            Entrance('old_chateau_e', 'OC Entrance E'),
            Entrance('old_chateau_s', 'OC Entrance S'),
            Entrance('old_chateau_w', 'OC Entrance W'),
            Entrance('old_chateau_c', 'OC Entrance C'),
        ]),
        Location('old_chatea_2f', 'Old Chateau 2F', [
            Entrance('old_chateau_2f_room_1', 'OC 2F Room 1'),
            Entrance('old_chateau_2f_room_2', 'OC 2F Room 2'),
            Entrance('old_chateau_2f_room_3', 'OC 2F Room 3'),
            Entrance('old_chateau_2f_room_4', 'OC 2F Room 4'),
            Entrance('old_chateau_2f_room_5', 'OC 2F Room 5'),
            Entrance('old_chateau_2f_exit', 'OC 2F Exit'),
        ]),
    ]),
    Category('solaceon_ruins', 'Solaceon Ruins', [
        Location('solaceon_ruins_1f', 'Solaceon Ruins 1F', [
            Entrance('solaceon_ruins_1f_nw', 'SR 1F NW'),
            Entrance('solaceon_ruins_1f_ne', 'SR 1F NE'),
            Entrance('solaceon_ruins_1f_se', 'SR 1F SE'),
            Entrance('solaceon_ruins_1f_exit', 'SR 1F Exit'),
        ]),
        Location('solaceon_ruins_b1f', 'Solaceon Ruins B1F', [
            Entrance('solaceon_ruins_b1f_nw', 'SR B1F NW'),
            Entrance('solaceon_ruins_b1f_ne', 'SR B1F NE'),
            Entrance('solaceon_ruins_b1f_se', 'SR B1F SE'),
            Entrance('solaceon_ruins_b1f_sw', 'SR B1F SW'),
        ]),
        Location('solaceon_ruins_b2f', 'Solaceon Ruins B2F', [
            Entrance('solaceon_ruins_b2f_nw', 'SR B2F NW'),
            Entrance('solaceon_ruins_b2f_ne', 'SR B2F NE'),
            Entrance('solaceon_ruins_b2f_se', 'SR B2F SE'),
            Entrance('solaceon_ruins_b2f_sw', 'SR B2F SW'),
        ]),
        Location('solaceon_ruins_b3f_a', 'Solaceon Ruins B3F A', [
            Entrance('solaceon_ruins_b3f_a_nw', 'SR B3F A NW'),
            Entrance('solaceon_ruins_b3f_a_ne', 'SR B3F A NE'),
            Entrance('solaceon_ruins_b3f_a_se', 'SR B3F A SE'),
            Entrance('solaceon_ruins_b3f_a_sw', 'SR B3F A SW'),
        ]),
        Location('solaceon_ruins_b3f_b', 'Solaceon Ruins B3F B', [
            Entrance('solaceon_ruins_b3f_b_nw', 'SR B3F B NW'),
            Entrance('solaceon_ruins_b3f_b_se', 'SR B3F B SE'),
            Entrance('solaceon_ruins_b3f_b_sw', 'SR B3F B SW'),
        ]),
        Location('solaceon_ruins_b4f', 'Solaceon Ruins B4F', [
            Entrance('solaceon_ruins_b4f_nw', 'SR B4F NW'),
            Entrance('solaceon_ruins_b4f_ne', 'SR B4F NE'),
            Entrance('solaceon_ruins_b4f_se', 'SR B4F SE'),
            Entrance('solaceon_ruins_b4f_sw', 'SR B4F SW'),
        ]),
    ]),
    Category('r208_forest_marsh', 'R208/Et.Forest/Marsh', [
        Location('r208', 'Route 208', [
            Entrance('r208_berry_house', 'R208 Berry House'),
            Entrance('r208_east_exit', 'R208 East Exit'),
            Entrance('r208_west_exit', 'R208 West Exit'),
        ]),
        Location('eterna_forest', 'Eterna Forest', [
            Entrance('eterna_forest_chateau', 'Eterna Forest Old Chateau'),
            Entrance('eterna_forest_east_exit', 'Eterna Forest East Exit'),
            Entrance('eterna_forest_west_exit', 'Eterna Forest South Exit'),
        ]),
        Location('great_marsh', 'Great Marsh', [
            Entrance('great_marsh_s', 'Great Marsh S'),
            Entrance('great_marsh_n', 'Great Marsh N'),
            Entrance('great_marsh_up', 'Great Marsh Up'),
        ])
    ]),
    Category('r213_214_222', 'R213/R214/R222', [
        Location('r213', 'Route 213', [
            Entrance('r213_hotel', 'R213 Hotel'),
            Entrance('r213_house', 'R213 House'),
            Entrance('r213_west_exit', 'R213 West Exit'),
        ]),
        Location('r214_hotel_222', 'R214/222/Hotel', [
            Entrance('r214_maniac_tunnel', 'R214 Maniac Tunnel'),
            Entrance('r214_north_exit', 'R214 North Exit'),
            Entrance('valor_lakefront', 'Valor Lakefront'),
            Entrance('hotel_grand_lake_nw', 'Hotel Grand Lake NW'),
            Entrance('hotel_grand_lake_n', 'Hotel Grand Lake N'),
            Entrance('hotel_grand_lake_ne', 'Hotel Grand Lake NE'),
            Entrance('hotel_grand_lake_w', 'Hotel Grand Lake W'),
            Entrance('hotel_grand_lake_e', 'Hotel Grand Lake E'),
            Entrance('hotel_grand_lake_se', 'Hotel Grand Lake SE'),
            Entrance('hotel_grand_lake_s', 'Hotel Grand Lake S'),
            Entrance('r222_house_w', 'R222 House W'),
            Entrance('r222_house_e', 'R222 House E'),
            Entrance('r222_east_exit', 'R222 East Exit'),
        ])
    ]),
    Category('mt_coronet', 'Mt Coronet', [
        Location('mt_coronet_1f_a', 'Coronet 1F A', [
            Entrance('mt_coronet_1f_a_north_stairs', 'Coronet 1F A North Stairs'),
            Entrance('mt_coronet_1f_a_east_exit', 'Coronet 1F A East Exit'),
            Entrance('mt_coronet_1f_a_south_exit', 'Coronet 1F A South Exit'),
            Entrance('mt_coronet_1f_a_west_exit', 'Coronet 1F A West Exit'),
        ]),
        Location('mt_coronet_1f_b', 'Coronet 1F B', [
            Entrance('mt_coronet_1f_b_south_stairs', 'Coronet 1F B South Stairs'),
            Entrance('mt_coronet_1f_b_regice_cave', 'Coronet 1F B Regice Cave'),
            Entrance('mt_coronet_1f_b_west_exit', 'Coronet 1F B West Exit'),
        ]),
        Location('mt_coronet_1f_c', 'Coronet 1F C', [
            Entrance('mt_coronet_1f_c_ne_stairs', 'Coronet 1F C NE Stairs'),
            Entrance('mt_coronet_1f_c_east_exit', 'Coronet 1F C East Exit'),
            Entrance('mt_coronet_1f_c_west_exit', 'Coronet 1F C West Exit'),
        ]),
        Location('mt_coronet_2f', 'Coronet 2F', [
            Entrance('mt_coronet_2f_s_stairs', 'Coronet 2F E Stairs'),
            Entrance('mt_coronet_2f_n_cave', 'Coronet 2F N Cave'),
            Entrance('mt_coronet_2f_sw_exit', 'Coronet 2F SW Exit'),
        ]),
        Location('mt_coronet_3f', 'Coronet 3F', [
            Entrance('mt_coronet_3f_east_stairs', 'Coronet 3F East Stairs'),
            Entrance('mt_coronet_3f_west_stairs', 'Coronet 3F West Stairs'),
            Entrance('mt_coronet_3f_west_exit', 'Coronet 3F West Exit'),
        ]),
        Location('mt_coronet_summit', 'Coronet Summit', [
            Entrance('mt_coronet_summit_nw_cave', 'Coronet Summit NW Cave'),
            Entrance('mt_coronet_summit_ne_cave', 'Coronet Summit NE Cave'),
            Entrance('mt_coronet_summit_e_cave', 'Coronet Summit E Cave'),
            Entrance('mt_coronet_summit_se_cave', 'Coronet Summit SE Cave'),
            Entrance('mt_coronet_summit_w_cave', 'Coronet Summit W Cave'),
            Entrance('mt_coronet_summit_sw_cave', 'Coronet Summit SW Cave'),
        ]),
    ]),
    Category('victory_road', 'Victory Road', [
        Location('victory_road_pc', 'VR PC', [
            Entrance('victory_road_pc_w', 'VR PC W'),
            Entrance('victory_road_pc_s', 'VR PC S'),
            Entrance('victory_road_pc_e', 'VR PC E'),
        ]),
        Location('pokemon_league_pc', 'League PC', [
            Entrance('pokemon_league_up', 'League PC Up'),
            Entrance('pokemon_league_down', 'League PC Down'),
            Entrance('pokemon_league_n', 'League PC N'),
            Entrance('pokemon_league_s', 'League PC S'),
        ]),
        Location('victory_road_1f', 'Victory Road 1F', [
            Entrance('victory_road_1f_nw_stairs', 'VR 1F NW Stairs'),
            Entrance('victory_road_1f_w_stairs', 'VR 1F W Stairs'),
            Entrance('victory_road_1f_sw_stairs', 'VR 1F SW Stairs'),
            Entrance('victory_road_1f_ne_stairs', 'VR 1F NE Stairs'),
            Entrance('victory_road_1f_e_stairs', 'VR 1F E Stairs'),
            Entrance('victory_road_1f_north_exit', 'VR 1F North Exit'),
            Entrance('victory_road_1f_east_cave', 'VR 1F East Cave'),
            Entrance('victory_road_1f_south_exit', 'VR 1F South Exit'),
        ]),
        Location('victory_road_b1f', 'Victory Road B1F', [
            Entrance('victory_road_b1f_nw_stairs', 'VR B1F NW Stairs'),
            Entrance('victory_road_b1f_w_stairs', 'VR B1F W Stairs'),
            Entrance('victory_road_b1f_sw_stairs', 'VR B1F SW Stairs'),
        ]),
    ]),
    Category('iron_island', 'Iron Island', [
        Location('iron_island_exterior', 'Iron Island Exterior', [
            Entrance('iron_island_exterior_entrance', 'Iron Island Exterior Entrance'),
            Entrance('iron_island_exterior_house', 'Iron Island Exterior House'),
            Entrance('iron_island_exterior_exit', 'Iron Island Exterior Exit'),
        ]),
        Location('iron_island_1f', 'Iron Island 1F', [
            Entrance('iron_island_1f_w', 'Iron Island 1F W'),
            Entrance('iron_island_1f_e', 'Iron Island 1F E'),
            Entrance('iron_island_1f_exit', 'Iron Island 1F Exit'),
        ]),
        Location('iron_island_b1f', 'Iron Island B1F', [
            Entrance('iron_island_b1f_nw', 'Iron Island B1F NW'),
            Entrance('iron_island_b1f_sw', 'Iron Island B1F SW'),
            Entrance('iron_island_b1f_se', 'Iron Island B1F SE'),
        ]),
        Location('iron_island_b3f', 'Iron Island B3F', [
            Entrance('iron_island_b3f_nw', 'Iron Island B3F NW'),
            Entrance('iron_island_b3f_n', 'Iron Island B3F N'),
            Entrance('iron_island_b3f_se', 'Iron Island B3F SE'),
        ]),
    ]),
    Category('poketch_gts_gate', 'Pokétch/GTS/Oreb. Gate', [
        Location('poketch_interior', 'Poketch Interior', [
            Entrance('poketch_interior_sw', 'Poketch Interior SW'),
            Entrance('poketch_interior_se', 'Poketch Interior SE'),
            Entrance('poketch_interior_up', 'Poketch Interior Up'),
        ]),
        Location('gts_1f', 'GTS 1F', [
            Entrance('gts_1f_warp_w', 'GTS 1F Warp W'),
            Entrance('gts_1f_warp_e', 'GTS 1F Warp E'),
            Entrance('gts_1f_exit', 'GTS 1F Exit'),
        ]),
        Location('oreburgh_gate', 'Oreburgh Gate', [
            Entrance('oreburgh_gate_stairs', 'Oreburgh Gate Stairs'),
            Entrance('oreburgh_gate_east_exit', 'Oreburgh Gate East Exit'),
            Entrance('oreburgh_gate_west_exit', 'Oreburgh Gate West Exit'),
        ]),
    ]),
    Category('surf_hub', 'Surf Hub', [
        Location('lake_verity', 'Lake Verity',
                 [Entrance('lake_verity', 'Lake Verity')]),
        Location('lake_valor', 'Lake Valor',
                 [Entrance('lake_valor', 'Lake Valor')]),
        Location('lake_acuity', 'Lake Acuity',
                 [Entrance('lake_acuity', 'Lake Acuity')]),
        Location('r221', 'Route 221', [
            Entrance('r221_house', 'R221 House'),
            Entrance('r221_pal_park', 'R221 Pal Park'),
        ]),
    ]),
]
