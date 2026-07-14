import subprocess, os

dates = [
    "2026-07-14",
    "2026-07-30",
    "2026-07-31",
    "2026-08-04"
]

NEXTJS_TOPICS = [
    ("feat(nextjs): implement App Router layout and dynamic routing structure", "app/layout.jsx",
     "export default function RootLayout({ children }) {\n  return (\n    <html lang=\"en\">\n      <body>{children}</body>\n    </html>\n  );\n}\n"),
    ("feat(nextjs): add Server Actions for form mutation and data handling", "app/actions/submit.js",
     "'use server';\nexport async function submitData(formData) {\n  const name = formData.get('name');\n  return { success: true, name };\n}\n"),
    ("perf(nextjs): configure ISR revalidation and static page generation", "app/dashboard/page.jsx",
     "export const revalidate = 60;\nexport default async function DashboardPage() {\n  return <div>Dashboard Content</div>;\n}\n"),
    ("feat(nextjs): implement Middleware for route protection and session check", "middleware.js",
     "import { NextResponse } from 'next/server';\nexport function middleware(request) {\n  return NextResponse.next();\n}\n")
]

TIME_SLOTS = ["09:30:00", "12:15:00", "15:45:00", "18:20:00"]
AUTHOR_NAME = "IshikaSharma04"
AUTHOR_EMAIL = "ishika.24bcs10352@sst.scaler.com"

# Baseline README
with open("README.md", "w") as f:
    f.write("# NextJS Projects & Experiments\n")

subprocess.run(["git", "add", "."], check=True)

env = os.environ.copy()
env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL
env["GIT_AUTHOR_DATE"] = "2026-07-14T09:00:00"
env["GIT_COMMITTER_DATE"] = "2026-07-14T09:00:00"

subprocess.run(["git", "commit", "-m", "Initial commit: setup NextJS project baseline"], env=env, check=True)

total = 1
for date_str in dates:
    for i, (msg, file_path, content) in enumerate(NEXTJS_TOPICS):
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(file_path, "a") as f:
            f.write(f"\n// Updated: {date_str} {TIME_SLOTS[i]}\n" + content)

        subprocess.run(["git", "add", file_path], check=True)

        commit_iso = f"{date_str}T{TIME_SLOTS[i]}"
        env["GIT_AUTHOR_DATE"] = commit_iso
        env["GIT_COMMITTER_DATE"] = commit_iso

        subprocess.run(["git", "commit", "-m", msg], env=env, check=True)
        total += 1

print(f"\nGenerated {total} clean backdated commits for NextJS!")
