SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
h_1 = int(input())
m_1 = int(input())
s_1 = int(input())
h_2 = int(input())
m_2 = int(input())
s_2 = int(input())
nb_of_seconds = SECONDS_IN_HOUR * (h_2 - h_1) + SECONDS_IN_MINUTE * (m_2 - m_1) + s_2 - s_1
print(nb_of_seconds)
