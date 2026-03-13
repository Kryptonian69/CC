# Check for Chocolatey
if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "Chocolatey is not installed. Software check will continue using existing tools." -ForegroundColor Yellow
}

# Function to install if missing
function Install-IfMissing($command, $package) {
    if (!(Get-Command $command -ErrorAction SilentlyContinue)) {
        Write-Host "$command not found. Attempting to install $package..." -ForegroundColor Cyan
        if (Get-Command choco -ErrorAction SilentlyContinue) {
            choco install $package -y
        } else {
            Write-Host "Please install $package manually: (Command '$command' not found)" -ForegroundColor Red
        }
    } else {
        Write-Host "$command is already installed." -ForegroundColor Green
    }
}

Install-IfMissing "node" "nodejs"
Install-IfMissing "java" "openjdk"
Install-IfMissing "dotnet" "dotnet-sdk"
Install-IfMissing "code" "vscode"
# Postman doesn't have a direct CLI command to check easily in standard PATH, 
# but we can assume it's there if the user said so, or just skip choco if unsure.

# Setup Node.js Service
Write-Host "Setting up Node.js Service..." -ForegroundColor Cyan
Set-Location "currency-conversion-service"
if (Test-Path "package.json") {
    npm install
} else {
    Write-Host "Error: package.json not found in currency-conversion-service" -ForegroundColor Red
}
Set-Location ..

# Setup .NET Client
Write-Host "Setting up .NET Client..." -ForegroundColor Cyan
Set-Location "NET_Client"
if (Test-Path "Program.cs") {
    Move-Item -Path "Program.cs" -Destination "Program.cs.bak" -Force
    dotnet new console --force
    Move-Item -Path "Program.cs.bak" -Destination "Program.cs" -Force
} else {
    dotnet new console
}
Set-Location ..

# Setup Java Client
Write-Host "Compiling Java Client..." -ForegroundColor Cyan
Set-Location "Java_Client"
if (Get-Command javac -ErrorAction SilentlyContinue) {
    javac JavaClient.java
} else {
    Write-Host "Java Compiler (javac) not found. Please ensure JDK is installed and in PATH." -ForegroundColor Red
}
Set-Location ..

Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "To run the service: cd currency-conversion-service; node server.js"
Write-Host "To run Java Client: cd Java_Client; java JavaClient"
Write-Host "To run .NET Client: cd NET_Client; dotnet run"
