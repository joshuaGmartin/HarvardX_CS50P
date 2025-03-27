results = ["Mario", "Luigi"]
print(results)

results.append("Peach")
print(results)

results.append("Toad")
print(results)

results.append("DK")
print(results)

# results = results + ["Daisy", "Yoshi", "Bowser"]
# print(results)

results.append(["Daisy", "Yoshi", "Bowser"])
print(results)
results.remove(["Daisy", "Yoshi", "Bowser"])

results.extend(["Daisy", "Yoshi", "Bowser"])
print(results)

results = ["Mario", "Luigi", "Peach", "Toad", "DK", "Daisy", "Yoshi", "Bowser"]
print(results)

results.remove("Bowser")
print(results)

results.insert(0, "Bowser")

results.reverse()
print(results)
