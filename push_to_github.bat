@echo off
echo ========================================================
echo Git Commit and Push Assistant - SkillPath AI
echo ========================================================
echo.

:: Check if git is initialized
if not exist .git (
    echo [ERROR] Git repository is not initialized.
    echo Running git init...
    git init
)

:: Prompt user for commit message
set /p commit_msg="Enter your commit message (default: 'feat: Complete SkillPath AI application'): "
if "%commit_msg%"=="" set commit_msg="feat: Complete SkillPath AI application"

echo.
echo Adding files...
git add .

echo.
echo Committing files...
git commit -m %commit_msg%

echo.
echo [SUCCESS] Committed changes successfully.
echo If you want to push to GitHub, add a remote origin:
echo   git remote add origin YOUR_REPOSITORY_URL
echo   git branch -M main
echo   git push -u origin main
echo.
pause
