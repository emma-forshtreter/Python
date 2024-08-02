import pytest
from string_utils import StringUtils

utils = StringUtils()

#Первая буква - заглавная

def test_capitilize():
#Позитивные тесты
    assert utils.capitilize('venus') == 'Venus'
    assert utils.capitilize('фёдор') == 'Фёдор'
    assert utils.capitilize('ура!') == 'Ура!'
#Негативные тесты
    assert utils.capitilize('12345') == '12345'
    assert utils.capitilize('& ^ @') == '& ^ @'
    
    
#Удаление пробела в начале текста

def test_trim():
#Позитивные тесты
    assert utils.trim('   text') == 'text'
    assert utils.trim('  12345') == '12345'
    assert utils.trim(' Как прекрасен этот мир') == 'Как прекрасен этот мир'
#Негативные тесты
    assert utils.trim('12345') == '12345'
    assert utils.trim('     text') == 'text'
    assert utils.trim('Text') == 'Text'
    
#Преобразование текста с разделителем в список строк

def test_to_list():
#Позитивные тесты
    assert utils.to_list('one,two,three') == ['one','two','three']
    assert utils.to_list('1,2,3,4,5') == ['1','2','3','4','5']
    assert utils.to_list('раз:два:три', ':') == ['раз','два','три']
#Негативные тесты
    assert utils.to_list('12345') == ['12345']
    assert utils.to_list('@ # $ % & *') == ['@ # $ % & *']
    assert utils.to_list('А Б Р А К А Д А Б Р А') == ['А Б Р А К А Д А Б Р А']
    
#Возвращает True, если строка содержит искомый символ и False - если нет

def test_contains():
#Позитивные тесты
    assert utils.contains('Yekaterinburg','Y') == True
    assert utils.contains('Yekaterinburg','W') == False
    assert utils.contains('123456567','7') == True
#Негативные тесты
    assert utils.contains(' ','Y') == False
    assert utils.contains('1234565','0') == False
    assert utils.contains('3','2') == False
    
#Удаление подстроки из переданной строки

def test_delete_symbol():
#Позитивные тесты
    assert utils.delete_symbol('Yekaterinburg','Y') == ('ekaterinburg')
    assert utils.delete_symbol('Yekaterinburg','burg') == ('Yekaterin')
    assert utils.delete_symbol('1234567','7') == ('123456')
#Негативные тесты
    assert utils.delete_symbol('Why','x') == ('Why')
    assert utils.delete_symbol('1234565','0') == ('1234565')
    assert utils.delete_symbol('3','2') == ('3')
    
#True, если строка начинается с заданного символа. False, если нет

def test_starts_with():
#Позитивные тесты
    assert utils.starts_with('Yekaterinburg','Y') == True
    assert utils.starts_with('Yekaterinburg','B') == False
    assert utils.starts_with('1234567','1') == True
#Негативные тесты
    assert utils.starts_with('Why','x') == False
    assert utils.starts_with('1234565','0') == False
    assert utils.starts_with('3','2') == False
    
#True, если строка заканчивается заданным символом. False, если нет

def test_end_with():
#Позитивные тесты
    assert utils.end_with('Yekaterinburg','g') == True
    assert utils.end_with('Yekaterinburg','Y') == False
    assert utils.end_with('1234567','7') == True
#Негативные тесты
    assert utils.end_with('Why','W') == False
    assert utils.end_with('1234565','1') == False
    assert utils.end_with('3','2') == False
    
#True, если строка пустая. False, если нет

def test_is_empty():
#Позитивные тесты
    assert utils.is_empty('') == True
    assert utils.is_empty('Yekaterinburg') == False
    assert utils.is_empty('1234567') == False
#Негативные тесты
    assert utils.is_empty('          ') == True
    assert utils.is_empty('@^ #&^') == False
    assert utils.is_empty('Здесь ничего нет') == False
    
#Преобразование списка элементов в строку с указанным разделителем

def test_list_to_string():
#Позитивные тесты
    assert utils.list_to_string(['Baden','Baden'],'-') == 'Baden-Baden'
    assert utils.list_to_string(['3','1415926535'],',') == '3,1415926535'
    assert utils.list_to_string([2,4,8,16,32]) == '2, 4, 8, 16, 32'
#Негативные тесты
    assert utils.list_to_string(['one','two','three'],' ') == 'one two three' 
    assert utils.list_to_string(['Здесь ничего нет']) == 'Здесь ничего нет'  