# ⚾ Baseball Website Project Setup Guide 網頁設置

> **Version Note:**  
> The project folder name follows the pattern **`website_v*`** —   
> the *number indicates the version*.  
> Use the **highest version number** for the latest release.


> **版本说明**：
> 项目文件夹名称遵循以下格式：**website_v*** —
> *数字表示版本*。
> 使用**最高版本号**表示最新版本。

## 文件名和位置
> Webscrape Python 代码以及数据排序代码位于 python_webscrape 文件夹中，以及 2025_07_26 抓取的数据。
> Webscrape 数据位于其他文件夹中。

## FILE NAMES & Location
> The webscrape python code along with the data sorting code is in the python_webscrape folder along with scraped data from 2025_07_26
> webscraped data is inside others 



## 📦 Download Instructions

To save space, you only need to **download the folder** named:
```
website_v*
```
(where `*` is the highest version number)

## 📦 下载说明

为了节省空间，您只需**下载名为**的文件夹：
```
website_v*
```
（其中 `*` 表示最高版本号）

## 🚀 Running the Server

1. **Navigate to the project folder:**
   ```bash
   cd website_v*
   ```

2. **Start the local server:**
   ```bash
   node server.js
   ```

3. Once you see:
   ```
   Server running at http://localhost:3000
   ```
   ✅ it means your server is running successfully!

4. Then, open the homepage using **Live Server** in VS Code (or your preferred method).

---

## ⚠️ Troubleshooting (Windows)

If the server doesn’t start correctly, make sure **Node.js** is installed.

### 🪟 Install Node.js (Windows)
Run this command in PowerShell:
```bash
winget install OpenJS.NodeJS
```

### ✅ Confirm installation
```bash
node -v   # shows Node.js version
npm -v    # shows npm (Node package manager) version
```

If both versions appear, you’re ready to go!

---

## 🧠 Quick Summary

| Step | Command / Action | Description |
|------|------------------|-------------|
| 1 | `cd website_v*` | Move into the latest version folder |
| 2 | `node server.js` | Start backend server |
| 3 | Open Live Server | View homepage (`index.html`) |
| 4 | Check terminal | Should show: `Server running at http://localhost:3000` |

---

### ✨ Tip
If you update your code, just stop and re-run the server:
```bash
Ctrl + C   # stop server
node server.js
```

---

## 🚀 运行服务器

1. **导航到项目文件夹：**
```bash
cd website_v*
```

2. **启动本地服务器：**
```bash
node server.js
```

3. 一旦看到：
```
服务器正在 http://localhost:3000 上运行
```
✅ 则表示您的服务器已成功运行！

4. 然后，使用 VS Code 中的 **Live Server**（或您喜欢的方法）打开主页。

---

## ⚠️ 故障排除（Windows）

如果服务器无法正常启动，请确保已安装 **Node.js**。

### 🪟 安装 Node.js (Windows)
在 PowerShell 中运行以下命令：
```bash
winget install OpenJS.NodeJS
```

### ✅ 确认安装
```bash
node -v # 显示 Node.js 版本
npm -v # 显示 npm（Node 包管理器）版本
```

如果两个版本都显示，则表示您已准备就绪！

---

## 🧠 快速摘要

| 步骤 | 命令/操作 | 描述 |
|------|------------------|-------------|
| 1 | `cd website_v*` | 移动到最新版本文件夹 |
| 2 | `node server.js` | 启动后端服务器 |
| 3 | 打开实时服务器 | 查看主页（`index.html`）|
| 4 | 检查终端 | 应显示：`Server running at http://localhost:3000` |

---

### ✨ 提示
如果您更新了代码，只需停止并重新运行服务器：
```bash
Ctrl + C # 停止服务器
node server.js
```

---

**Author:** 劉晨煜  
**Project:** CPBL Baseball Website  
**Language:** Node.js + HTML + JavaScript + CSS + python + json


