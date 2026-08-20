# 手順7：利用テストで見つかった迷いを、一か所だけ直す。
# 見つかった迷い：「18人」と出ても、行くか待つかを決められなかった。
import pandas as pd
import streamlit as st

st.title("購買、いつ行く？")

jikoku = st.radio("何時に行く？", ["12:35", "12:40", "12:45"])

kiroku = pd.read_csv("kounai_queue.csv")
onaji_jikoku = kiroku[kiroku["時刻"] == jikoku]
yosou = onaji_jikoku["並んでいた人数"].mean()
saidai = onaji_jikoku["並んでいた人数"].max()
saishou = onaji_jikoku["並んでいた人数"].min()

st.metric("並んでいる人数の予想", f"{yosou:.0f}人")
st.caption(f"{len(onaji_jikoku)}日ぶんの記録から。少ない日は{saishou}人、多い日は{saidai}人。")

# 直した一か所：人数だけでなく、次の行動を出す。
if yosou >= 15:
    st.warning("いま行くと並ぶ。5分後の記録も見てから決める。")
else:
    st.success("この時刻なら、昼休み中に買って戻れた日が多い。")

st.bar_chart(onaji_jikoku.set_index("日付")["並んでいた人数"])
st.caption("この記録は、授業で数えた5日ぶんだけ。学校行事の日や雨の日は入っていない。")
