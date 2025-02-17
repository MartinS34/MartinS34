# Analyzing Drug Effectiveness Using Weighted and Bayesian Ratings

## 📌 Overview
This academic project explores different methods to measure **drug effectiveness** using:
- **Weighted Ratings** (adjusted by useful counts)
- **Bayesian Scaling** (which favors drugs with more reviews)
- **Average Ratings** (traditional approach)

## 🛠 Tech/Tools Used
- **Shell Scripting (`cut`, `awk`)** – Extracted and processed drug review data.
- **Python (Google Colab, Matplotlib)** – Visualized effectiveness ratings.
- **Data Manipulation (TSV/CSV Processing)** – Cleaned and structured data.

## 📊 Methodology
1. Extracted **10 most common conditions** from the dataset using the `cut` command.
2. Used `awk` to **copy reviews** of these conditions into a separate file.
3. Wrote **two shell scripts**:
   - `wr.sh`: Calculates **weighted ratings** by multiplying each review’s rating by its useful count.
   - `ar.sh`: Computes a **simple average rating** for each drug.
4. Implemented the **Bayesian Rating Formula** to adjust for the number of reviews.
5. Visualized **Weighted Ratings vs Average Ratings** for ADHD drugs in **Google Colab**.

## 📈 Key Findings
- **Weighted ratings** provide a **more accurate effectiveness measure** than simple averages.
- **Bayesian scaling** favors drugs with **higher review counts**, reducing bias.
- **Unexpected Result**: Bupropion, a **non-stimulant drug**, was more well received than stimulant ADHD drugs.

## 📑 Final Report
For a full summary of findings and methodology, check out the project report:

📄 [View the Final Findings Report](findings.pdf)


## 📂 Project Files
- [`wr.sh`](wr.sh) → Computes **weighted ratings** for each drug.
- [`ar.sh`](ar.sh) → Computes **average ratings** for each drug.
- [`top5.sh`](top5.sh) → Extracts the **top 5 highest-rated drugs**.
- [`drug_data.tsv`](drug_data.tsv) → Original dataset containing drug reviews.
- [`top_5_drugs.tsv`](top_5_drugs.tsv) → Filtered dataset of top-rated drugs.
- [`a5-Visualization.ipynb`](a5-Visualization.ipynb) → Py file for data visualization of cleaned data


## 🔗 Repository
**View this project live in my portfolio:**  
👉 [CS-131 Drug Effectiveness Analysis](https://MartinS34.github.io/projects/cs131-a5)

---
