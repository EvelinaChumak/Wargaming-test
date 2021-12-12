import pytest
from tests.config.info_for_tables import SHIPS_COUNT
from tests.config.mes_in_assert import CHANGE_COMP, CHANGE_PARAM
import tests.config.info_for_tables as Table
from framework.utils.tuple_fuc import TupleFuc

class Test():
    
    @pytest.mark.parametrize('index', 
                             [index for index in range (1, SHIPS_COUNT+1)])
    def test_weapon(self, index, connect_and_fill_db, 
                connect_and_change_copy_db):
        first_params = pytest.db.get_ship_info('weapon', index)
        second_params = pytest.copy_db.get_ship_info('weapon', index)
        ship, first_weapon = first_params[0]
        second_weapon = second_params[0][1]
        
        first_com = pytest.db.get_weapon_info(second_weapon)
        second_com = pytest.copy_db.get_weapon_info(second_weapon)
        param_index = TupleFuc.get_diff_index(first=first_com[0],
                                              second=second_com[0])
        param = Table.WEAPONS_VALUES[param_index]
        assert first_com == second_com, CHANGE_PARAM.format(
                                        ship, second_weapon,
                                        param, 
                                        first_com[0][param_index],
                                        second_com[0][param_index])
        
        assert first_params == second_params, CHANGE_COMP.format(
                                              ship, second_weapon, 
                                              first_weapon, second_weapon)
    
    @pytest.mark.parametrize('index', 
                             [index for index in range (1, SHIPS_COUNT+1)])
    def test_hull(self, index, connect_and_fill_db, 
                connect_and_change_copy_db):
        first_params = pytest.db.get_ship_info('hull', index)
        second_params = pytest.copy_db.get_ship_info('hull', index)
        ship, first_hull = first_params[0]
        second_hull = second_params[0][1]
        
        first_com = pytest.db.get_hull_info(second_hull)
        second_com = pytest.copy_db.get_hull_info(second_hull)
        param_index = TupleFuc.get_diff_index(first=first_com[0],
                                              second=second_com[0])
        param = Table.HULLS_VALUES[param_index]
        
        assert first_com == second_com, CHANGE_PARAM.format(
                                        ship, second_hull,
                                        param, 
                                        first_com[0][param_index],
                                        second_com[0][param_index])
        
        assert first_params == second_params, CHANGE_COMP.format(
                                              ship, second_hull, 
                                              first_hull, second_hull)

    @pytest.mark.parametrize('index', 
                             [index for index in range (1, SHIPS_COUNT+1)])
    def test_engine(self, index, connect_and_fill_db, 
                connect_and_change_copy_db):
        first_params = pytest.db.get_ship_info('engine', index)
        second_params = pytest.copy_db.get_ship_info('engine', index)
        ship, first_engine = first_params[0]
        second_engine = second_params[0][1]
  
        first_com = pytest.db.get_engine_info(second_engine)
        second_com = pytest.copy_db.get_engine_info(second_engine)
        param_index = TupleFuc.get_diff_index(first=first_com[0],
                                              second=second_com[0])
        param = Table.ENGINES_VALUES[param_index]
        
        assert first_com == second_com, CHANGE_PARAM.format(
                                        ship, second_engine,
                                        param, 
                                        first_com[0][param_index],
                                        second_com[0][param_index])
        
        assert first_params == second_params, CHANGE_COMP.format(
                                              ship, second_engine, 
                                              first_engine, second_engine)
