---
title: Sums over zeros near the line of convergence
decls:
  - GlobalTheory.Lin.ZeroSum.sum_rpow_zeros_le
  - GlobalTheory.T.exists_sum_characters_finsum_zeros_rpow_re_sub_one_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Sums over zeros near the line of convergence

In the explicit formula for primes in progressions, each zero $\rho$ of $L(s, \chi)$ contributes a term of size $u^{\mathrm{Re}\,\rho}/|\rho|$. After division by the main term $u$, one has to bound the sum of $u^{\mathrm{Re}\,\rho - 1}$ over the zeros of all characters modulo $q$ up to height $T$. This section proves such a bound from [the log-free zero density estimate](/entry/zero-density/). If all zeros satisfy $\mathrm{Re}\,\rho \leq 1 - \eta$, the sum is at most $C(u^{-\eta/2} + u^{-\eta_0})$, as soon as $u$ is a fixed power of $qT$. There is no factor for the number of zeros. The bound is used in Section 6, in the proof of [the relative error for $\psi(u; M, b)$](/entry/psi-ap-relative/).

We keep the notation of Section 4: $Z(\chi; \sigma, T)$ is the set of zeros $\rho$ of $L(s, \chi)$ with $\sigma \leq \mathrm{Re}\,\rho < 1$ and $|\mathrm{Im}\,\rho| \leq T$, $\mathrm{ord}_\rho$ is the order of the zero, and $D(\chi; c, R)$ is the set of zeros in the closed disc of radius $R$ about $c$, without the point $1$ for the principal character.

The proof needs a crude bound for the total number of zeros in the box, for the zeros far from the line $\mathrm{Re}\, s = 1$. It comes from the following result on the logarithmic derivative, which is proved elsewhere in the development.

**Theorem 2.5.1 (Zeros near a point of the line $\mathrm{Re}\, s = 2$).** There is $C > 0$ such that for every $q$, every $\chi$ modulo $q$, every real $t$, every $\sigma$ with $1 < \sigma \leq 2$ and every $k \geq 0$, the set $D(\chi; 2 + it, 3)$ is finite, and
$$\begin{aligned} \sum_{w \in D(\chi; 2 + it, 3)} \mathrm{ord}_w &\leq C\log(q(|t| + 2)), \\ \Bigl| D_k(\chi; s) - \frac{\delta_\chi}{(s - 1)^{k+1}} + \sum_{w \in D(\chi; 2 + it, 3)} \frac{\mathrm{ord}_w}{(s - w)^{k+1}} \Bigr| &\leq \frac{C\log(q(|t| + 2))}{\sigma^k}, \end{aligned}$$
where $s = \sigma + it$, $\delta_\chi = 1$ for the principal character and $0$ otherwise, and $D_k$ is the series of Section 4.

Lean: `GlobalTheory.T.iteratedDeriv_logDeriv_dirichletL_via_nearby_zeros`.

Only the first inequality is used here. It is the classical bound for the number of zeros in a disc of bounded radius, which follows from Jensen's formula (see Davenport, Chapter 16).

**Lemma 2.5.2 (Total number of zeros).** There is $C > 0$ such that for every $q$, every $\chi$ modulo $q$ and every $T \geq 2$, the set $Z(\chi; 1/2, T)$ is finite and
$$\sum_{\rho \in Z(\chi; 1/2, T)} \mathrm{ord}_\rho \leq C q T^2.$$

Lean: `GlobalTheory.Lin.ZeroSum.total_count`.

*Proof.* Let $\rho \in Z(\chi; 1/2, T)$ and $m = \lfloor \mathrm{Im}\,\rho \rfloor$. Then $|m| \leq \lceil T \rceil$, and $|\rho - (2 + im)| \leq 3/2 + 1 \leq 3$. Also $\rho \neq 1$, as $\mathrm{Re}\,\rho < 1$. So $\rho \in D(\chi; 2 + im, 3)$. There are at most $2\lceil T \rceil + 1$ values of $m$. For each, the theorem bounds the weight of the disc by $C\log(q(T + 3))$. The product is at most a constant times $qT^2$. $\square$

**Lemma 2.5.3 (Layers).** Let $s$ be a finite set with weights $w_i \geq 0$ and real numbers $\delta_i$. Let $L > 0$, $\eta \geq 0$ and $e$ be real, and let $J$ be an integer with $J > Le$. Then
$$\begin{aligned} \sum_{\substack{i \in s \\ \delta_i \geq \eta}} w_i e^{-L\delta_i} &\leq \sum_{j = 0}^{J - 1} e^{-L\eta - j} \sum_{\substack{i \in s \\ \delta_i \leq \min(\eta + (j+1)/L,\, e)}} w_i \; + \; e^{-Le}\sum_{i \in s} w_i. \end{aligned}$$

Lean: `GlobalTheory.Lin.ZeroSum.layers`.

*Proof.* Let $i \in s$ with $\delta_i \geq \eta$. If $\delta_i > e$, the term is at most $e^{-Le}w_i$. Otherwise let $j \geq 0$ be the integer with $\eta + j/L \leq \delta_i < \eta + (j+1)/L$. Then $j \leq L\delta_i \leq Le < J$, the term is at most $e^{-L\eta - j}w_i$, and $i$ is counted in the $j$-th inner sum. $\square$

**Theorem 2.5.4 (Sums over zeros).** There are $A, C, \eta_0 > 0$ with the following property. Let $q \geq 1$, $T \geq 2$, $u \geq (qT)^A$ and $\eta \geq 0$. Then
$$\sum_{\chi \bmod q}\ \sum_{\substack{\rho \in Z(\chi; 1/2, T) \\ \mathrm{Re}\,\rho \leq 1 - \eta}} \mathrm{ord}_\rho\, u^{\mathrm{Re}\,\rho - 1} \leq C\bigl(u^{-\eta/2} + u^{-\eta_0}\bigr).$$

Lean: `GlobalTheory.Lin.ZeroSum.sum_rpow_zeros_le` (also `GlobalTheory.T.exists_sum_characters_finsum_zeros_rpow_re_sub_one_le`, a second name).

*Proof.* Let $A_1, C_1, \eta_1$ be the constants of [the log-free zero density estimate](/entry/zero-density/), and $C_2$ that of the lemma on the total number. Choose $e$ with $0 < e \leq \min(\eta_1, 1/2)$. We take
$$A = 2A_1 + \frac{4}{e}, \qquad \eta_0 = \frac{e}{2}.$$
Put $\mathcal{L} = \log u$ and $\mathcal{M} = \log(qT)$. Then $qT \geq 2$, and $u \geq (qT)^A$ gives $2A_1\mathcal{M} \leq \mathcal{L}$ and $4\mathcal{M} \leq e\mathcal{L}$. For a zero $\rho$ put $\delta_\rho = 1 - \mathrm{Re}\,\rho$, so that $u^{\mathrm{Re}\,\rho - 1} = e^{-\mathcal{L}\delta_\rho}$. The condition $\mathrm{Re}\,\rho \leq 1 - \eta$ is $\delta_\rho \geq \eta$.

Fix $\chi$ and apply the layer lemma to $Z(\chi; 1/2, T)$ with weights $\mathrm{ord}_\rho$, with $L = \mathcal{L}$ and with an integer $J > \mathcal{L}e$. Then sum over $\chi$.

The layers. For $0 \leq j < J$ put $x_j = \min(\eta + (j+1)/\mathcal{L}, e)$. The zeros with $\delta_\rho \leq x_j$ are the elements of $Z(\chi; 1 - x_j, T)$. Since $x_j \leq e \leq \eta_1$, the density estimate applies with $\sigma = 1 - x_j$:
$$\sum_\chi \sum_{\delta_\rho \leq x_j} \mathrm{ord}_\rho \leq C_1 (qT)^{A_1 x_j} = C_1 e^{A_1\mathcal{M}x_j} \leq C_1 e^{\mathcal{L}x_j/2} \leq C_1 e^{\mathcal{L}\eta/2 + (j+1)/2}.$$
So the $j$-th layer contributes at most $C_1 e^{1/2}\, e^{-\mathcal{L}\eta/2}\, e^{-j/2}$. Summing over $j$ gives at most $C_1 e^{1/2} K u^{-\eta/2}$, with $K = \sum_{j \geq 0} e^{-j/2}$.

The rest. There are at most $q$ characters modulo $q$. By the lemma on the total number, the last term is at most
$$e^{-\mathcal{L}e} \cdot q \cdot C_2 q T^2 \leq C_2\, e^{-\mathcal{L}e + 2\mathcal{M}} \leq C_2\, e^{-\mathcal{L}e/2} = C_2\, u^{-\eta_0},$$
since $2\mathcal{M} \leq e\mathcal{L}/2$.

So the theorem holds with $C = C_1 e^{1/2}K + C_2$. $\square$

The two terms of the bound have different roles. The term $u^{-\eta/2}$ comes from the zeros close to the line $\mathrm{Re}\, s = 1$, which the density estimate counts without loss. The term $u^{-\eta_0}$ comes from all other zeros, and it is small because $u$ is a large power of $qT$.

**Remark 2.5.5 (Formalization).** The theorem on zeros near $2 + it$ is a separate formal result, proved elsewhere in the development, and we have not checked its proof. The fact that each zero lies in one of the discs is the lemma `GlobalTheory.Lin.ZeroSum.mem_disc` ([SumRpowZerosLe.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/SumRpowZerosLe.lean#L10)). The sum over zeros is a finite sum because the box contains only finitely many zeros; this finiteness is part of the lemma on the total number. The wrapper `GlobalTheory.T.exists_sum_characters_finsum_zeros_rpow_re_sub_one_le` is stated in a file of its own and proved by citing the theorem.
