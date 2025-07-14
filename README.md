# Dự án: Huấn luyện Mô hình Nhận diện Khuôn mặt GhostFaceNet trên Dữ liệu Glint360k với Distributed Data Parallel (DDP)

Chào mừng đến với repository cho dự án huấn luyện mô hình nhận diện khuôn mặt GhostFaceNet trên bộ dữ liệu khổng lồ Glint360k sử dụng PyTorch và chiến lược huấn luyện phân tán Distributed Data Parallel (DDP).

## Giới thiệu

Dự án này tập trung vào việc triển khai và thực hiện quá trình huấn luyện một mô hình nhận diện khuôn mặt tiên tiến, cụ thể là GhostFaceNet, trên một trong những bộ dữ liệu nhận diện khuôn mặt lớn nhất hiện có, Glint360k. Với quy mô lên tới 17 triệu ảnh, việc huấn luyện hiệu quả đòi hỏi sử dụng tính toán phân tán. Dự án này tận dụng Distributed Data Parallel (DDP) của PyTorch để tăng tốc độ và khả năng mở rộng quy mô huấn luyện trên nhiều GPU hoặc nhiều máy chủ.

## Các Tính năng chính

*   **Huấn luyện GhostFaceNet:** Triển khai kiến trúc mô hình GhostFaceNet.
*   **Bộ dữ liệu Glint360k:** Hỗ trợ tải và xử lý bộ dữ liệu Glint360k với 17 triệu ảnh và 360k danh tính.
*   **Distributed Data Parallel (DDP):** Sử dụng PyTorch DDP cho phép huấn luyện phân tán hiệu quả trên nhiều thiết bị.
*   **Tăng tốc Huấn luyện:** Giảm thời gian huấn luyện bằng cách tận dụng sức mạnh tính toán song song.
*   **Khả năng mở rộng:** Thiết lập dễ dàng mở rộng để huấn luyện trên các cụm máy lớn hơn.

## Bộ dữ liệu: Glint360k

Bộ dữ liệu Glint360k là một bộ dữ liệu nhận diện khuôn mặt quy mô lớn, bao gồm khoảng 17 triệu ảnh thuộc 360,000 danh tính. Đây là một thách thức lớn cho việc huấn luyện các mô hình nhận diện khuôn mặt mạnh mẽ và có khả năng khái quát hóa tốt.

**Lưu ý:** Do kích thước lớn, bạn sẽ cần tải xuống và chuẩn bị bộ dữ liệu Glint360k trước khi bắt đầu huấn luyện. Vui lòng tham khảo hướng dẫn chuẩn bị dữ liệu (sẽ được cung cấp hoặc liên kết trong phần sau).

## Yêu cầu

*   Python 3.6+
*   PyTorch (phiên bản hỗ trợ DDP, khuyến nghị phiên bản mới nhất)
*   torchvision
*   Các thư viện Python khác (xem `requirements.txt`)
*   GPU(s) hỗ trợ CUDA (cần thiết cho việc huấn luyện phân tán)
*   Dung lượng đĩa trống đủ để lưu trữ bộ dữ liệu Glint360k.

## Cài đặt

1.  Clone repository:
    ```bash
    git clone https://github.com/namkuner/Distributed_GhostFaceNet_Train_on_Glint360k.git
    cd Distributed_GhostFaceNet_Train_on_Glint360k
    ```

2.  Cài đặt các thư viện cần thiết:
    ```bash
    pip install -r requirements.txt
    ```

3.  Đảm bảo PyTorch được cài đặt với hỗ trợ CUDA.

## Chuẩn bị Dữ liệu

Bạn cần tải xuống bộ dữ liệu Glint360k. Thông thường, bộ dữ liệu này có sẵn dưới dạng các file `.idalgo` hoặc định dạng tương tự.

1.  **Tải xuống:** Tải xuống bộ dữ liệu Glint360k từ nguồn cung cấp. (Cần thêm chi tiết về nguồn nếu có thể).
2.  **Giải nén/Chuyển đổi:** Chuyển đổi dữ liệu sang định dạng phù hợp cho PyTorch `Dataset`, ví dụ như tập hợp các thư mục ảnh hoặc file `.rec`/`.idx`. (Cung cấp script hoặc hướng dẫn cụ thể ở đây).
3.  **Cấu trúc Thư mục:** Đảm bảo cấu trúc thư mục dữ liệu của bạn tuân thủ cách load dữ liệu trong code. Ví dụ:
    ```
    /path/to/glint360k/
        class_id_000001/
            image_0001.jpg
            image_0002.jpg
            ...
        class_id_000002/
            image_0001.jpg
            ...
        ...
    ```
4.  Cập nhật đường dẫn dữ liệu trong file cấu hình của bạn.

## Cấu hình Huấn luyện

Các tùy chọn huấn luyện (ví dụ: tốc độ học, số epoch, kích thước batch, đường dẫn dữ liệu, v.v.) có thể được cấu hình thông qua các tham số dòng lệnh hoặc một file cấu hình (ví dụ: `config.yaml` hoặc các tham số trong script huấn luyện).

Kiểm tra các script huấn luyện (`train.py` hoặc tương tự) để biết các tùy chọn cấu hình có sẵn.

## Huấn luyện

Dự án này sử dụng PyTorch's `torchrun` (hoặc `torch.distributed.launch` trên các phiên bản PyTorch cũ hơn) để chạy huấn luyện phân tán.

**Huấn luyện trên nhiều GPU trên một máy:**

Sử dụng lệnh `torchrun` và chỉ định số lượng processes (= số GPU bạn muốn sử dụng).

```bash
torchrun --nproc_per_node=NUM_GPUS train.py --data_path /path/to/glint360k/ --other_args ...
kết quả train https://api.wandb.ai/links/namkunerr/2r9zatha
