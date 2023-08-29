<h1 align="center">Flask Portfolio Template</h1>
<p align="center">
  <i>Craft your digital presence with Flask. A comprehensive portfolio template to showcase your work and insights.</i>
  <br/>
  <img width="120" src="https://raw.githubusercontent.com/buildwithdan/flask-portfolio/simple/api/static/images/flask.png" />
  <br/>
  <b><a href="http://danienell.com">User Showcase</a></b> | <b><a href="https://hub.docker.com/r/buildwithdan/flask-portfolio">Docker Image</a></b> | <b><a href="https://github.com/buildwithdan/flask-portfolio/blob/simple/LICENSE.md">License</a></b>
  <br/><br/>
  <a href="https://visitor-badge.laobi.icu/badge?page_id=buildwithdan.flask-portfolio">
    <img src="https://visitor-badge.laobi.icu/badge?page_id=buildwithdan.flask-portfolio" alt="Visitor Badge">
  </a>
  <a href="https://vercel.com/new/clone?repository-url=https://github.com/buildwithdan/flask-portfolio">
    <img src="https://vercel.com/button" alt="Deploy with Vercel">
  </a>
  <a href="https://github.com/buildwithdan/flask-portfolio/blob/simple/LICENSE.md">
    <img src="https://img.shields.io/badge/License-MIT-0aa8d2?logo=opensourceinitiative&logoColor=fff" alt="License MIT">
  </a>
  <a href="https://hub.docker.com/r/buildwithdan/flask-portfolio">
    <img src="https://img.shields.io/docker/pulls/buildwithdan/flask-portfolio?logo=docker&color=0aa8d2&logoColor=fff" alt="Docker Pulls">
  </a>
</p>


## 🛠️ Stack

- **Framework**: [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- **Styling**: [Bootstrap](https://getbootstrap.com/)
- **Deployment**: [Vercel](https://vercel.com)
- **Analytics**: [Vercel Analytics](https://vercel.com/analytics)

## 🗂️ Directory & Configuration

### `config.ini`

Located under `api/config.ini`, this configuration file lets you input key information such as:

- Name
- Email
- Domain
- Social media links

By populating this file, you enable the automatic update of the entire Flask app with your personal information. Ensure to fill out every detail correctly to reflect your identity throughout the app.

## ✅ TODO

- [x] Add comments to the blog (completed: 2023.08.11)
- [x] Create `config.ini` for all variables (completed: 2023.08.11)

## 📝 Using Markdown for Blog and Project Posts

Utilize the provided templates for creating content:

- [Blog post template](https://github.com/buildwithdan/flask-portfolio/tree/simple/api/content/blogs)
- [Project post template](https://github.com/buildwithdan/flask-portfolio/tree/simple/api/content/projects)

For assistance with markdown syntax, visit [Markdown Live Preview](https://markdownlivepreview.com/).

### Blog Post Structure
[Example Here](https://raw.githubusercontent.com/buildwithdan/flask-portfolio/simple/api/content/blogs/Blog-1.md?token=GHSAT0AAAAAACAGIQ5MGJYUPQFFRHX2RDR6ZBLBG7A)

### Activating Blog Comments

1. Create a new public repo named `my-blog-comments`.
2. Enter `YourGithubName/my-blog-comments` inside [Config.ini](https://github.com/buildwithdan/flask-portfolio/tree/simple/api/config.ini).
3. Test your first post which will prompt you to install the app, directing it to your `my-blog-comments` repo.

> Credit: [https://utteranc.es/](https://utteranc.es/)

### Project Post Structure
[Example Here](https://raw.githubusercontent.com/buildwithdan/flask-portfolio/simple/api/content/projects/project-1.md?token=GHSAT0AAAAAACAGIQ5MPUJGDAFDBRJUIJXYZBLBGOQ)

## 🚀 Local Development

Ensure you have the latest versions of Python and Flask. Then, follow these steps:

```bash
git clone https://github.com/buildwithdan/flask-portfolio.git
cd flask-portfolio
flask --debug --app api/index.py run
```

## 🐳 Docker Deployment

> **Note**: This Docker setup was crafted primarily for educational purposes. If you intend to modify website content, clone or fork the [original project](https://github.com/buildwithdan/flask-portfolio), then adjust the HTML files under `api/templates`. Subsequently, rebuild the Docker image for deployment.

To build the Docker image, use:

```bash
docker build -t appname .
```

### Docker Run Command

Replace the following paths to your own local machine folders you created, to allow docker to use your own markdown files:  
"/path/to/blogs" 
"/path/to/projects"

```bash
docker run -d \
  --name=flask-portfolio \
  -p 5002:5000 \
  -v /path/to/blogs:/app/api/content/blogs \
  -v /path/to/projects:/app/api/content/projects \
  --restart unless-stopped \
  buildwithdan/flask-portfolio
```

As example:
```bash
docker run -d \
  --name=flask-portfolio \
  -p 5002:5000 \
  -v /home/root/website/blogs:/app/api/content/blogs \
  -v /home/root/website/projects:/app/api/content/projects \
  --restart unless-stopped \
  buildwithdan/flask-portfolio
```

For detailed Docker CLI info, [refer to the official documentation](https://docs.docker.com/engine/reference/commandline/cli/).

## 🍴 Cloning / Forking

Kindly consult the [license](https://github.com/buildwithdan/flask-portfolio/blob/simple/LICENSE.md) and erase all personal details (resume, blog entries, images, etc.) from your cloned/forked version.
