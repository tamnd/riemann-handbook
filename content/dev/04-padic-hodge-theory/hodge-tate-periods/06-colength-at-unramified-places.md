---
title: Colength at unramified places
decls:
  - GlobalTheory.ChF.linDat_unram_bound
  - GlobalTheory.T.linearData_unramified_length_bound
  - GlobalTheory.ChF.unramified_companion_chart_characters
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Colength at unramified places

This section gives the second colength bound, for a place $w$ of $E$ above $p$ when $p$ is odd and unramified in $E$. The place need not be split. Here the embeddings of $w$ form one orbit under Frobenius, and the bound at the embedding $\tau_j$ is a weighted sum over the Frobenius orbit. The weight of the $n$-th step is $p^{-n}$, and the term is the eigenspace dimension at the conjugate embedding. As in [the split case](/entry/colength-bound-split-place-chart/), we prove the bound first for a [linear datum](/entry/exists-lin-dat-of-ext-ser/), and then for the formal group of a degenerating abelian scheme. The second form is used directly in the step [every character of the literature](/step/every-character-of-literature/).

We keep the setting and the definitions of [the previous section](/entry/colength-bound-lin-dat/): places, lengths, eigenbases and the restriction $\mathrm{res}_W$. In addition, $\mathcal{O}$ is a local ring with maximal ideal $\mathfrak{m}$. For a ring map $\tau : O_E \to \mathcal{O}$ write $\bar\tau = \tau \circ {}^*$ for the conjugate embedding.

### Frobenius orbits

Let $w$ be a place above $p$, that is, a nonzero primitive idempotent $e$ of $O_e$, and let $n = \operatorname{rank}_{\mathbb{Z}_p} eO_e$. We do not ask that $e$ is split. An enumeration $\tau_1, \dots, \tau_n$ of the embeddings of $e$ is *Frobenius ordered* if
$$\tau_{j+1}(a) \equiv \tau_j(a)^p \pmod{\mathfrak{m}} \quad \text{for all } a \in O_E \text{ and all } j,$$
with indices modulo $n$. If $p$ is unramified in $E$, then the completion $O_w$ is the ring of [[Witt vectors|6N3X2QX4W9]] of a finite field of degree $n$ over $\mathbb{F}_p$. Its embeddings into $\mathcal{O}$ are permuted cyclically by the Frobenius, so a Frobenius ordered enumeration exists.

For an eigenspace dimension function $r$ on embeddings and an index $j$, put
$$\Sigma_j(r) = \sum_{k=0}^{\infty} p^{-(k+1)}\, r\bigl(\bar\tau_{j+k+1}\bigr).$$
The sequence $r(\bar\tau_{j+k+1})$ is periodic of period $n$, so the series converges. If $r$ is constant equal to $h$ on the conjugate embeddings, then $\Sigma_j(r) = h/(p-1)$, since $\sum_{k \geq 0} p^{-(k+1)} = 1/(p-1)$.

### The bound for linear data

**Theorem 4.6.1 (Colength at an unramified place, linear form).** Let $p$ be odd, let $c_p \in \mathcal{O}$, and let $H$ be a Hodge-Tate datum over $\mathcal{O}$ for $(O_e, \sigma, c_p)$ in a Hodge-Tate setting. Let $(H, A, B, \rho_G, N, s)$ be a linear datum with $s_1, \dots, s_m \in \mathcal{O}^d$. Assume that $p$ does not divide the discriminant of $O_E$ over $\mathbb{Z}$. Let $w$ be a place above $p$ with $n \geq 1$, and let $\tau_1, \dots, \tau_n$ be a Frobenius ordered enumeration of its embeddings. For each ring map $\tau : O_E \to \mathcal{O}$ let $W_\tau$ be a $\tau$-eigenbasis of $\rho_G$ with $r(\tau)$ elements. Then for each $j$ there is a length $x_j$ of $\mathcal{O}^{r(\tau_j)}/\langle \mathrm{res}_{W_{\tau_j}}(s_k) : k \leq m \rangle$ with
$$v(p)^{\Sigma_j(r)} \leq x_j.$$

Lean: `GlobalTheory.ChF.linDat_unram_bound` (also `GlobalTheory.T.linearData_unramified_length_bound`, a second name).

*Proof.* Write $\lambda = v(p)$, so $0 < \lambda < 1$.

First, the unramified decomposition. Since $p$ does not divide the discriminant and $P = P_L = 0$, there is a finite family of ring maps $\sigma_i : O_e \to \mathcal{O}$, one for each embedding of $O_E$, with complete families of orthogonal idempotent matrices $\varepsilon_T(i)$ on $\mathcal{O}^{\mathrm{Ix}}$ and $\varepsilon_L(i)$ on $\mathcal{O}^g$. The matrices $\rho(a)$ and $\rho_L(a)$ act on the images of $\varepsilon_T(i)$ and $\varepsilon_L(i)$ by $\sigma_i(a)$. There is a permutation $i \mapsto \bar i$ with $\sigma_{\bar i} = \sigma_i \circ \sigma$ and a Frobenius permutation $\varphi$ with $v(\sigma_{\varphi(i)}(a) - \sigma_i(a)^p) < 1$. Distinct indices are distinct modulo $\mathfrak{m}$. The image of $\varepsilon_L(i)$ is free of a rank $r_L(i)$. Let $i_j$ be the index of $\tau_j$. Since distinct indices are distinct modulo $\mathfrak{m}$, the Frobenius order gives $\varphi(i_j) = i_{j+1}$, so $\varphi^k(i_j) = i_{j+k}$.

Second, the Tate module. The ring $O_w$ is monogenic, and $\rho$ makes $\mathbb{Z}_p^{\mathrm{Ix}}$ a free $O_w$-module of some rank $h$ on its $w$-part. So the $\tau_k$-eigenspace of $\rho$ over $C$ has dimension $h$ for each $k$. The Hodge-Tate datum splits this eigenspace into the parts at $\tau_k$ and at $\bar\tau_k$ of the cotangent space, so $r_L(i_k) + r_L(\bar i_k) = h$.

Third, the comparison with $\rho_G$. Since $(A, B)$ is split exact and intertwines $\rho_G$ with $N$ and $\rho_L$, the eigenspace dimension of $\rho_G$ at $\sigma_i$ is that of $N$ plus that of $\rho_L$. So $r_L(i) \leq r(\tau)$ for the embedding $\tau$ of index $i$. Also $r(\tau) \leq d$ for all $\tau$.

Fourth, the cokernel. Let $\mathrm{cok}_j$ be the quotient of the image of $\varepsilon_L(i_j)^{\mathsf T}$ by its intersection with $H$ applied to the image of $\varepsilon_T(\bar i_j)$. It has a length $V$, and it maps onto the module $\mathcal{O}^{r(\tau_j)}/\langle \mathrm{res}_{W_{\tau_j}}(s_k) \rangle$. A surjection can only increase the length, so $V \leq x_j$.

Fifth, the unramified cokernel bound. For odd $p$ in a Hodge-Tate setting,
$$\lambda^{\frac{r_L(i_j) + r_L(\bar i_j)}{p-1} - \sum_{k \geq 0} p^{-(k+1)} r_L(\varphi^{k+1}(i_j))} \leq V.$$

Sixth, the exponent. By the first two steps, $r_L(\varphi^{k+1}(i_j)) = r_L(i_{j+k+1}) = h - r_L(\bar i_{j+k+1})$. So
$$\frac{h}{p-1} - \sum_{k \geq 0} p^{-(k+1)} r_L(i_{j+k+1}) = \sum_{k \geq 0} p^{-(k+1)} r_L(\bar i_{j+k+1}) \leq \Sigma_j(r)$$
by the third step. Since $\lambda < 1$, a larger exponent gives a smaller power, so $\lambda^{\Sigma_j(r)} \leq V \leq x_j$. $\square$

### The bound for degenerating abelian schemes

We use the setting of the chart form of [the split case](/entry/colength-bound-split-place-chart/): $T$, the group $G$ with degeneration data, the chart with formal group law $F$, the compatible actions of $O_E$, the local map $\iota : T \to \mathcal{O}$, and the linear parts $\rho^\iota(a)$ of the action over $\mathcal{O}$.

**Theorem 4.6.2 (Colength at an unramified place, chart form).** In this setting, let $p$ be odd, assume that $p$ does not divide the discriminant of $O_E$, and let $\mathcal{O}$ be local. Let $w$ be a place above $p$ with $n \geq 1$, and let $\tau_1, \dots, \tau_n$ be a Frobenius ordered enumeration of its embeddings. Assume that there is a $\mathbb{Z}_p$-basis $b_1, \dots, b_n$ of $O_w$ with $\det(\tilde\tau_j(b_i))$ a unit. For each ring map $\tau : O_E \to \mathcal{O}$ let $W_\tau$ be a $\tau$-eigenbasis of $\rho^\iota$ with $r(\tau)$ elements. Then for each $j$ there are characters $u_1, \dots, u_m$ of $F^\iota$ and a length $x_j$ of $\mathcal{O}^{r(\tau_j)}/\langle \mathrm{res}_{W_{\tau_j}}(du_k) : k \leq m \rangle$ with
$$v(p)^{\Sigma_j(r)} \leq x_j.$$

Lean: `GlobalTheory.ChF.unramified_companion_chart_characters`.

*Proof.* As in the chart form of [the split case](/entry/colength-bound-split-place-chart/), the uniformization makes $F^\iota$ an extension of the formal group law of the abelian part by $\hat{\mathbb{G}}_m^r$, with finite flat $p$-power torsion and equivariant for $O_E$. The polarized abelian part gives a Hodge-Tate datum and characters. So [the theorem on split extensions](/entry/exists-lin-dat-of-ext-ser/) gives a linear datum whose covectors are differentials of characters $u_k$ of $F^\iota$, with $\rho_G = \rho^\iota$. The eigenbases of $\rho^\iota$ are eigenbases of $\rho_G$, and the linear form gives $x_j$. $\square$

**Remark 4.6.3 (Formalization).** The hypothesis that the determinant $\det(\tilde\tau_j(b_i))$ is a unit is not used: the proof binds it to an unnamed variable at [UnramifiedCompanionChartCharacters.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/UnramifiedCompanionChartCharacters.lean#L34), and the linear form has no such hypothesis. For $p$ unramified the hypothesis holds anyway. Both forms ask for an eigenbasis $W_\tau$ at every ring map $\tau : O_E \to \mathcal{O}$, not only at the embeddings of $w$ and their conjugates; the bound at $\tau_j$ uses $r$ only at $\tau_j$ and at the conjugates $\bar\tau_k$. The second name of the linear form is proved by `first | exact @GlobalTheory.ChF.linDat_unram_bound | ...` at [LinearDataUnramifiedLengthBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/LinearDataUnramifiedLengthBoundStatement.lean#L21), with a raised heartbeat limit at line 19, and the chart form calls this second name. The fifth step is a separate theorem of the development, which the proof uses as given.
