import streamlit as st

st.set_page_config(page_title="Кастомный калькулятор", layout="centered")

st.title("🧮 Кастомный калькулятор")

base_value = st.number_input("🔢 Базовая стоимость", value=0.0)

if "fields" not in st.session_state:
    st.session_state.fields = [{"title": "Поле 1", "value": 0.0, "operation": "+"}]

if "last_result" not in st.session_state:
    st.session_state.last_result = None
    st.session_state.last_expression = ""

if st.button("➕ Добавить поле"):
    st.session_state.fields.append(
        {"title": f"Поле {len(st.session_state.fields) + 1}", "value": 0.0, "operation": "+"})

if len(st.session_state.fields) > 1 and st.button("🗑 Удалить последнее поле"):
    st.session_state.fields.pop()

st.markdown("### Ввод данных")

for i, field in enumerate(st.session_state.fields):
    col1, col2, col3 = st.columns([2, 2, 1])
    title = col1.text_input(f"Название {i + 1}", value=field["title"], key=f"title_{i}")
    value = col2.number_input(f"Значение {i + 1}", value=field["value"], key=f"value_{i}")
    operation = col3.selectbox(
        "Операция", ["+", "-", "*", "/", "%"], index=["+", "-", "*", "/", "%"].index(field["operation"]), key=f"op_{i}"
    )

    # Сохраняем обновления
    st.session_state.fields[i] = {"title": title, "value": value, "operation": operation}

if st.button("📊 Показать результат"):
    result = base_value
    expression = f"{base_value}"
    for field in st.session_state.fields:
        op = field["operation"]
        val = field["value"]
        if op == "+":
            result += val
        elif op == "-":
            result -= val
        elif op == "*":
            result *= val
        elif op == "/":
            result /= val if val != 0 else 1
        elif op == "%":
            result += result * (val / 100)
        expression += f" {op} {val}"

    st.session_state.last_result = result
    st.session_state.last_expression = expression

if st.session_state.last_result is not None:
    st.markdown("### Результат")
    st.write(f"{st.session_state.last_expression} = **{st.session_state.last_result}**")
