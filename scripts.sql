CREATE TABLE dbo.Users (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Email NVARCHAR(150) NOT NULL,
    CreatedAt DATETIME NOT NULL DEFAULT GETDATE()
);
GO

-----------------------

CREATE PROCEDURE dbo.usp_user_create
    @Name NVARCHAR(100),
    @Email NVARCHAR(150)
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO dbo.Users (Name, Email)
    VALUES (@Name, @Email);

    SELECT SCOPE_IDENTITY() AS Id;
END;
GO

---------------------

CREATE PROCEDURE dbo.usp_user_list
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        Id,
        Name,
        Email,
        CreatedAt
    FROM dbo.Users
    ORDER BY Id DESC;
END;
GO


----------------------

CREATE PROCEDURE dbo.usp_user_get_by_id
    @Id INT
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        Id,
        Name,
        Email,
        CreatedAt
    FROM dbo.Users
    WHERE Id = @Id;
END;
GO
