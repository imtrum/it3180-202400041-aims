# Git Workflow Discussion

## 1. Vì sao dùng `git mv`?

- Di chuyển hoặc đổi tên file và tự động cập nhật Staging Area.
- Giúp thao tác rõ ràng, tránh quên `git add`.
- Git nhận diện rename dựa trên sự tương đồng nội dung file, không dựa vào một lệnh rename đặc biệt.

## 2. `release/lab01` có phải baseline không?

- Baseline là phiên bản cơ sở dùng làm mốc tham chiếu.
- `release/lab01` có thể là baseline nếu nhóm quy định nó lưu phiên bản hoàn chỉnh của Lab 01.
- Tên branch không tự động quyết định vai trò baseline.

## 3. Vì sao không commit thẳng vào `master` dù làm một mình?

- Bảo vệ branch chính khỏi code chưa hoàn thiện.
- Có thể kiểm tra code và chạy test qua PR.
- Giúp quản lý lịch sử và dễ dàng hoàn tác thay đổi.

## 4. Vì sao phải đồng bộ `master` trước khi PR?

- Cập nhật những thay đổi mới nhất từ `master`.
- Phát hiện và xử lý conflict sớm.
- Đảm bảo tính năng tương thích với code hiện tại.

```bash
git fetch origin
git merge origin/master
```

## 5. Khi nào không được rebase?

- Khi branch đã được chia sẻ và người khác đang sử dụng.
- Khi branch là branch dùng chung như `master`, `develop`, `release/*`.
- Khi việc viết lại lịch sử có thể ảnh hưởng đến thành viên khác.

**Nguyên tắc:** Không rebase lịch sử đã chia sẻ nếu chưa thống nhất với nhóm.

## 6. `feature/*` khác `topic/*` ra sao?

- `feature/*`: Dùng để phát triển tính năng mới.
- `topic/*`: Dùng cho một nhóm thay đổi theo chủ đề, có thể là feature, bugfix hoặc refactor.

Đây là quy ước đặt tên, không phải hai loại branch đặc biệt của Git.

## 7. Merge base là gì?

- Là commit tổ tiên chung gần nhất của hai branch.
- Git sử dụng merge base để xác định những thay đổi khi merge.

```bash
git merge-base master feature
```

## 8. Vì sao `master` / `release/*` phải dùng revert?

- Đây là các branch dùng chung, cần bảo toàn lịch sử.
- `reset` viết lại lịch sử, có thể ảnh hưởng đến người khác.
- `revert` tạo commit mới để đảo ngược thay đổi mà không xóa lịch sử cũ.

```bash
git revert <commit-sha>
```

Nếu hoàn tác merge commit:

```bash
git revert -m 1 <merge-commit-sha>
```

**Nguyên tắc:** Branch cá nhân có thể reset; branch dùng chung nên ưu tiên revert.

## 9. Vì sao `release/*` không merge vào `master`?

- Trong workflow của project, `release/*` được sử dụng làm baseline hoặc mốc tham chiếu cho từng Lab.
- Đây không phải branch dùng để chuẩn bị production release.
- Merge chúng vào `master` có thể đưa code cũ hoặc thay đổi không cần thiết vào branch chính.
- Các feature và bugfix được tích hợp vào `master` thông qua Pull Request.
- Khi hoàn thành release, tạo tag trên commit đã được duyệt của `master`.

**Lưu ý:** Đây là quy ước riêng của project, không phải quy tắc chung của Git. Trong GitFlow, release branch thường được merge vào cả `master` và `develop`.

## 10. So sánh workflow của project với GitFlow

| Tiêu chí | Project workflow | GitFlow |
|---|---|---|
| Branch chính | `master` | `master` và `develop` |
| Feature branch | `feature/*`, `topic/*` | `feature/*` |
| Release branch | Làm baseline cho từng Lab | Chuẩn bị phiên bản release |
| Hotfix branch | Tùy workflow | `hotfix/*` |
| Release process | PR vào `master`, sau đó tạo tag | Merge release vào `master` và `develop` |

- GitFlow có cấu trúc branch phức tạp và rõ ràng hơn.
- Workflow của project đơn giản hơn, phù hợp với quy mô bài thực hành.
- Hai workflow có mục đích và quy ước sử dụng branch khác nhau.

## 11. Vì sao lên phiên bản `1.0.0` mà không phải `0.4.0`?

Theo Semantic Versioning (SemVer), phiên bản có cấu trúc:

`MAJOR.MINOR.PATCH`

- `0.x.x`: Giai đoạn phát triển ban đầu, API chưa được xem là ổn định.
- `1.0.0`: Phiên bản stable đầu tiên, đánh dấu project đã sẵn sàng.
- `0.4.0`: Vẫn thuộc giai đoạn phát triển trước phiên bản stable.

Nếu AIMS-mini đã hoàn thành các chức năng dự kiến và được xem là ổn định, chọn `1.0.0` thể hiện đây là phiên bản stable đầu tiên.

**Kết luận:** Việc chọn phiên bản phụ thuộc vào mức độ hoàn thiện và cam kết về tính ổn định của project, không phụ thuộc đơn thuần vào số lượng Lab đã hoàn thành.
