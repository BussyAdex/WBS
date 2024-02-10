import os
import json
from fastapi import APIRouter, status
import schemas


router = APIRouter(
    prefix='/wbs',
    tags=['WBSRecords']
)

@router.get('/{day}/{category}', status_code=status.HTTP_200_OK)
def get_data(day: int, category: str) -> list:
    current_directory = os.getcwd()
    file_name = f'2023-06-{day}.json'
    file_path = os.path.join(current_directory, 'data', file_name)

    if not os.path.exists(file_path):
        return "File does not exist for the day selected"

    with open(file_path, 'r') as data:
        result = json.load(data)
        data_for_category = result[category]
        return data_for_category


@router.post('/{day}/{category}', status_code= status.HTTP_201_CREATED)
def set_data(day:int, category:str, data_in:schemas.wbsData)->list:
    current_directory = os.getcwd()
    file_name = f'2023-06-{day}.json'
    file_path = os.path.join(current_directory, 'data', file_name)

    if not os.path.exists(file_path):
        return "File does not exist for the day selected"

    with open(file_path, 'r') as data:
        result = json.load(data)
        data_for_category = result[category]
        data_for_category.append(data.model_dump())
        return data_in.model_dump()