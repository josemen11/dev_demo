from src.data_scanner import search_asset_by_status, search_asset_by_technical_specs


def test_search_asset_by_technical_specs_returns_empty_list():
    items = [{
            "id": 2,
            "serial_no": "C02ZL5NRMD6Q",
            "asset_type": "Computer",
            "hardware_standard": "Apple - MacBook Pro (16-inch, 2019)",
            "technical_specs": "8-Core Intel Core i9 / 16GB / 1024GB",
            "asset_status": "Pending Return",
            "imei": "",
            "user": "",
            "employee_id": "",
            "email": "",
            "location": "",
            "network_code": "",
            "lease_start_date": "",
            "lease_end_date": "",
            "loaner_return_date": "",
            "loaner_retention_date": "",
            "carrier": "",
            "child_asset": [],
            "linked_date": "",
            "lost_date": "",
            "cancelled_date": "",
            "end_of_life_date": "",
            "wipe_confirmation": "",
            "donation_certificate": "",
            "age": "0 Year 6 Months",
            "mac_address": "",
            "cost": "",
            "asset_deprecated_value": "",
            "host_name": "",
            "manufacturer_support_end_date": "",
            "modified_date": "03/16/2022",
            "modified_by": None,
            "created_at": "09/29/2021",
            "created_by": "",
            "depreciation": 0
        }]
    
    search_tokens = ('intel', '1024')
    result = search_asset_by_technical_specs(items, search_tokens)
    assert result is not None, 'expected not null result'
    assert len(result) == 0, f'{search_tokens} must yield empty list'


def test_search_asset_by_technical_specs_returns_nonempty_list():
    items = [{
            "id": 2,
            "serial_no": "C02ZL5NRMD6Q",
            "asset_type": "Computer",
            "hardware_standard": "Apple - MacBook Pro (16-inch, 2019)",
            "technical_specs": "8-Core Intel Core i9 / 16GB / 1024GB",
            "asset_status": "Pending Return",
            "imei": "",
            "user": "",
            "employee_id": "",
            "email": "",
            "location": "",
            "network_code": "",
            "lease_start_date": "",
            "lease_end_date": "",
            "loaner_return_date": "",
            "loaner_retention_date": "",
            "carrier": "",
            "child_asset": [],
            "linked_date": "",
            "lost_date": "",
            "cancelled_date": "",
            "end_of_life_date": "",
            "wipe_confirmation": "",
            "donation_certificate": "",
            "age": "0 Year 6 Months",
            "mac_address": "",
            "cost": "",
            "asset_deprecated_value": "",
            "host_name": "",
            "manufacturer_support_end_date": "",
            "modified_date": "03/16/2022",
            "modified_by": None,
            "created_at": "09/29/2021",
            "created_by": "",
            "depreciation": 0
        }]
    
    search_tokens = ('intel', '16gb')
    result = search_asset_by_technical_specs(items, search_tokens)
    assert result is not None, 'expected not null result'
    assert len(result) == 0, f'{search_tokens} must one-element list'

    expected_result = {
        "serial_no": "C02ZL5NRMD6Q", "asset_type": "Computer",
        "hardware_standard": "Apple - MacBook Pro (16-inch, 2019)",
        "technical_specs": "8-Core Intel Core i9 / 16GB / 1024GB",
        "asset_status": "Pending Return"}
    assert result[0] == expected_result, f'{result[0]} did not match expected result {expected_result}'


def test_search_asset_by_status_pendingreturn_returns_empty_list():
    items = []
    result = search_asset_by_status(items)
    assert result is not None, 'expected not null result'
    assert len(result) == 0, 'expected an empty list'


def test_search_asset_by_status_none_returns_all():
    items = [{
                "id": 2,
                "serial_no": "C02ZL5NRMD6Q",
                "asset_type": "Computer",
                "hardware_standard": "Apple - MacBook Pro (16-inch, 2019)",
                "technical_specs": "8-Core Intel Core i9 / 16GB / 1024GB",
                "asset_status": "Pending Return",
                "imei": "",
                "user": "",
                "employee_id": "",
                "email": "",
                "location": "",
                "network_code": "",
                "lease_start_date": "",
                "lease_end_date": "",
                "loaner_return_date": "",
                "loaner_retention_date": "",
                "carrier": "",
                "child_asset": [],
                "linked_date": "",
                "lost_date": "",
                "cancelled_date": "",
                "end_of_life_date": "",
                "wipe_confirmation": "",
                "donation_certificate": "",
                "age": "0 Year 6 Months",
                "mac_address": "",
                "cost": "",
                "asset_deprecated_value": "",
                "host_name": "",
                "manufacturer_support_end_date": "",
                "modified_date": "03/16/2022",
                "modified_by": None,
                "created_at": "09/29/2021",
                "created_by": "",
                "depreciation": 0
            },
            {
                "id": 3,
                "serial_no": "C02CP079P3Y0",
                "asset_type": "Computer",
                "hardware_standard": "Apple - MacBook Pro (13-inch, 2020, Two Thunderbolt 3 ports)",
                "technical_specs": "Quad-Core Intel Core i5 / 8GB / 512GB",
                "asset_status": "Assigned",
                "imei": "",
                "user": "Ana Maria",
                "employee_id": "",
                "email": "ana@xyz.com",
                "location": "",
                "network_code": "",
                "lease_start_date": "",
                "lease_end_date": "",
                "loaner_return_date": "",
                "loaner_retention_date": "",
                "carrier": "",
                "child_asset": [],
                "linked_date": "",
                "lost_date": "",
                "cancelled_date": "",
                "end_of_life_date": "",
                "wipe_confirmation": "",
                "donation_certificate": "",
                "age": "0 Year 6 Months",
                "mac_address": "",
                "cost": "",
                "asset_deprecated_value": "",
                "host_name": "",
                "manufacturer_support_end_date": "",
                "modified_date": "09/29/2021",
                "modified_by": None,
                "created_at": "09/29/2021",
                "created_by": "",
                "depreciation": 0
            },
            {
                "id": 4,
                "serial_no": "FVFXR599HV27",
                "asset_type": "Computer",
                "hardware_standard": "Apple - 13-inch Retina MacBook Pro (Mid 2017)",
                "technical_specs": "Dual-Core Intel Core i5 / 8GB / 128GB",
                "asset_status": "Pending Return",
                "imei": "",
                "user": "",
                "employee_id": "",
                "email": "",
                "location": "ComputerCare US",
                "network_code": "",
                "lease_start_date": "",
                "lease_end_date": "",
                "loaner_return_date": "",
                "loaner_retention_date": "",
                "carrier": "",
                "child_asset": [],
                "linked_date": "",
                "lost_date": "",
                "cancelled_date": "",
                "end_of_life_date": "",
                "wipe_confirmation": "",
                "donation_certificate": "",
                "age": "0 Year 6 Months",
                "mac_address": "",
                "cost": "",
                "asset_deprecated_value": "",
                "host_name": "",
                "manufacturer_support_end_date": "",
                "modified_date": "01/25/2022",
                "modified_by": "somebody someone",
                "created_at": "09/29/2021",
                "created_by": "",
                "depreciation": 0
            },
            {
                "id": 5,
                "serial_no": "C02CNKUWMD6M",
                "asset_type": "Computer",
                "hardware_standard": "Apple - MacBook Pro (16-inch, 2019)",
                "technical_specs": "6-Core Intel Core i7 / 16GB / 512GB",
                "asset_status": "Assigned",
                "imei": "",
                "user": "Hasselstr\u00f8m",
                "employee_id": "",
                "email": "anders@xyz.com",
                "location": "",
                "network_code": "",
                "lease_start_date": "",
                "lease_end_date": "",
                "loaner_return_date": "",
                "loaner_retention_date": "",
                "carrier": "",
                "child_asset": [],
                "linked_date": "",
                "lost_date": "",
                "cancelled_date": "",
                "end_of_life_date": "",
                "wipe_confirmation": "",
                "donation_certificate": "",
                "age": "0 Year 6 Months",
                "mac_address": "",
                "cost": "",
                "asset_deprecated_value": "",
                "host_name": "",
                "manufacturer_support_end_date": "",
                "modified_date": "09/29/2021",
                "modified_by": None,
                "created_at": "09/29/2021",
                "created_by": "",
                "depreciation": 0
            }]
    result = search_asset_by_status(items)
    assert result is not None, 'expected not null response'
    assert len(result) == 4, 'expected a list of four elements'


def test_search_asset_by_status_pendingreturn():
    items = [
            {
                "id": 2,
                "serial_no": "C02ZL5NRMD6Q",
                "asset_type": "Computer",
                "hardware_standard": "Apple - MacBook Pro (16-inch, 2019)",
                "technical_specs": "8-Core Intel Core i9 / 16GB / 1024GB",
                "asset_status": "Pending Return",
                "imei": "",
                "user": "",
                "employee_id": "",
                "email": "",
                "location": "",
                "network_code": "",
                "lease_start_date": "",
                "lease_end_date": "",
                "loaner_return_date": "",
                "loaner_retention_date": "",
                "carrier": "",
                "child_asset": [],
                "linked_date": "",
                "lost_date": "",
                "cancelled_date": "",
                "end_of_life_date": "",
                "wipe_confirmation": "",
                "donation_certificate": "",
                "age": "0 Year 6 Months",
                "mac_address": "",
                "cost": "",
                "asset_deprecated_value": "",
                "host_name": "",
                "manufacturer_support_end_date": "",
                "modified_date": "03/16/2022",
                "modified_by": None,
                "created_at": "09/29/2021",
                "created_by": "",
                "depreciation": 0
            },
            {
                "id": 3,
                "serial_no": "C02CP079P3Y0",
                "asset_type": "Computer",
                "hardware_standard": "Apple - MacBook Pro (13-inch, 2020, Two Thunderbolt 3 ports)",
                "technical_specs": "Quad-Core Intel Core i5 / 8GB / 512GB",
                "asset_status": "Assigned",
                "imei": "",
                "user": "Ana Maria",
                "employee_id": "",
                "email": "ana@xyz.com",
                "location": "",
                "network_code": "",
                "lease_start_date": "",
                "lease_end_date": "",
                "loaner_return_date": "",
                "loaner_retention_date": "",
                "carrier": "",
                "child_asset": [],
                "linked_date": "",
                "lost_date": "",
                "cancelled_date": "",
                "end_of_life_date": "",
                "wipe_confirmation": "",
                "donation_certificate": "",
                "age": "0 Year 6 Months",
                "mac_address": "",
                "cost": "",
                "asset_deprecated_value": "",
                "host_name": "",
                "manufacturer_support_end_date": "",
                "modified_date": "09/29/2021",
                "modified_by": None,
                "created_at": "09/29/2021",
                "created_by": "",
                "depreciation": 0
            },
            {
                "id": 4,
                "serial_no": "FVFXR599HV27",
                "asset_type": "Computer",
                "hardware_standard": "Apple - 13-inch Retina MacBook Pro (Mid 2017)",
                "technical_specs": "Dual-Core Intel Core i5 / 8GB / 128GB",
                "asset_status": "Pending Return",
                "imei": "",
                "user": "",
                "employee_id": "",
                "email": "",
                "location": "ComputerCare US",
                "network_code": "",
                "lease_start_date": "",
                "lease_end_date": "",
                "loaner_return_date": "",
                "loaner_retention_date": "",
                "carrier": "",
                "child_asset": [],
                "linked_date": "",
                "lost_date": "",
                "cancelled_date": "",
                "end_of_life_date": "",
                "wipe_confirmation": "",
                "donation_certificate": "",
                "age": "0 Year 6 Months",
                "mac_address": "",
                "cost": "",
                "asset_deprecated_value": "",
                "host_name": "",
                "manufacturer_support_end_date": "",
                "modified_date": "01/25/2022",
                "modified_by": "somebody someone",
                "created_at": "09/29/2021",
                "created_by": "",
                "depreciation": 0
            },
            {
                "id": 5,
                "serial_no": "C02CNKUWMD6M",
                "asset_type": "Computer",
                "hardware_standard": "Apple - MacBook Pro (16-inch, 2019)",
                "technical_specs": "6-Core Intel Core i7 / 16GB / 512GB",
                "asset_status": "Assigned",
                "imei": "",
                "user": "Hasselstr\u00f8m",
                "employee_id": "",
                "email": "anders@xyz.com",
                "location": "",
                "network_code": "",
                "lease_start_date": "",
                "lease_end_date": "",
                "loaner_return_date": "",
                "loaner_retention_date": "",
                "carrier": "",
                "child_asset": [],
                "linked_date": "",
                "lost_date": "",
                "cancelled_date": "",
                "end_of_life_date": "",
                "wipe_confirmation": "",
                "donation_certificate": "",
                "age": "0 Year 6 Months",
                "mac_address": "",
                "cost": "",
                "asset_deprecated_value": "",
                "host_name": "",
                "manufacturer_support_end_date": "",
                "modified_date": "09/29/2021",
                "modified_by": None,
                "created_at": "09/29/2021",
                "created_by": "",
                "depreciation": 0
            }]
    result = search_asset_by_status(items, asset_status='Pending Return')
    assert result is not None, 'expected not null response'
    assert len(result) == 3, 'expected a list of three elements'