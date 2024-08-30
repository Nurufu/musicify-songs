local fileList = fs.list("files")
print("Please enter the base URL")
local baseURL = read()
local data = {}
for i,o in pairs(fileList) do
  print("File: " .. o)
  data[i] = {}
  data[i].file = baseURL .. o
  local h = http.get(baseURL .. o:sub(1, -6) .. ".lrc")
  if h then
    data[i].lyrics = baseURL .. o:sub(1, -6) .. ".lrc"
    h.close()
  end
  data[i].type = "song"
  
  print("What is the artist?")
  data[i].author = read()
  print("What is the song name?")
  data[i].name = read()
end

local file = fs.open("data.json", "w")
file.write(textutils.serializeJSON(data))
file.close()
print("Done!")