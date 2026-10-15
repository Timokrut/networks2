import math
import matplotlib.pyplot as plt

packet_sizes = range(1, 50001)
fragments = [math.ceil((x + 8) / 1480) for x in packet_sizes]

plt.figure(figsize=(10, 6))
plt.plot(packet_sizes, fragments)

plt.xlabel("Размер ICMP данных, байт")
plt.ylabel("Количество фрагментов")
plt.title("Зависимость количества IPv4-фрагментов от размера ping-пакета")

plt.grid(True)
plt.show()