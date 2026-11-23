---
title: Hodge-Tate jumps through a cover
decls:
  - GlobalTheory.CovClose.closed_of_cover
  - GlobalTheory.T.isDeRham_of_breuilKisinFrame_isDeRham
  - GlobalTheory.T.isCrys_of_crystallineBreuilKisinFrame
  - GlobalTheory.T.adaptedBasis_theta_galoisFixed_poles
  - GlobalTheory.T.breuilKisinPreframe_bounded_poles
  - GlobalTheory.T.theta_conj_bounded_compatible_breuilKisin_frames
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hodge-Tate jumps through a cover

This section proves the theorem that the chapter was built for. Let $r : G_K \to \mathrm{GL}_a(\Omega)$ have a cover, in the sense of the previous section, whose members are semistable with the same Hodge-Tate jumps. Then $r$ is de Rham with these jumps, and it is crystalline when all members are. The de Rham property passes to the limit through [frames of bounded height](/entry/exists-frame-sst/) and [the limit of a tower of frames](/entry/limit-frame-exists/). The jumps pass to the limit through the traces of the Hodge-Tate operators of the previous section, which the frames bound uniformly. The theorem is used in the proof of [the theorem on closedness at $\ell$](/entry/closed-at-l/). We keep the notation of the previous section. First we state four lemmas on frames: two that read the de Rham and crystalline properties off a frame, and two that attach bounded operators on $C^d$ to a frame and compare them along links.

**Lemma 3.7.1 (De Rham frames).** Let $\tau$ be a Frobenius period and $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ a homomorphism. If $\rho$ has a de Rham [frame](/entry/semistable-period-frame/) of some height, then $\mathbb{Q}_\ell^d$ with $\rho$ is de Rham.

Lean: `GlobalTheory.T.isDeRham_of_breuilKisinFrame_isDeRham`.

**Lemma 3.7.2 (Crystalline frames).** Let $\tau$ and $\rho$ be as in the last lemma. If $\rho$ has a crystalline frame of some height, then $\mathbb{Q}_\ell^d$ with $\rho$ is crystalline.

Lean: `GlobalTheory.T.isCrys_of_crystallineBreuilKisinFrame`.

**Lemma 3.7.3 (Operators from de Rham frames).** Assume that $B_{\mathrm{dR}}^{G_{K''}} = K''$ for every finite extension $K''$ of $\mathbb{Q}_\ell$. Let $\tau$ be a Frobenius period, $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ a map, $F$ a de Rham frame of height $N$ for $\rho$ with basis $T$ and cocycle $\varepsilon$, and $Y \in M_d(A_{\mathrm{inf}})$ with $Y = \tau^N T$ in $M_d(W(C^\flat))$. Let $(V_H, p, q, Q)$ be a Hodge basis of $\rho$ for $\xi = E$ over $K$. Then for all $g$ and $z$ as in the lemma on a Galois element (without the condition on roots of unity) there is $u \in M_d(C)$ with
$$u \, \theta(Y) = \theta(Y) \, \theta(\varepsilon(g)), \qquad u \, \theta(V_H) = \theta(V_H) \, \mathrm{diag}(z^{p_1 - q}, \dots, z^{p_d - q}).$$

Lean: `GlobalTheory.T.adaptedBasis_theta_galoisFixed_poles`.

**Lemma 3.7.4 (Bounded poles).** Let $\tau$ be a Frobenius period. For every Breuil-Kisin basis $T$ of height $N$ for a map $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ there are $Y, Y' \in M_d(A_{\mathrm{inf}})$ with $Y = \tau^N T$ in $M_d(W(C^\flat))$ and $YY' = \tau^{2N}$.

Lean: `GlobalTheory.T.breuilKisinPreframe_bounded_poles`.

**Lemma 3.7.5 (A uniform bound).** Let $\tau$ be a Frobenius period and $N \geq 0$. There is a real number $B$ with the following property. Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ and $\rho' : G_K \to M_{d'}(\mathbb{Z}_\ell)$ be maps with frames $F$ and $F'$ of height $N$, with bases $T, T'$ and cocycles $\varepsilon, \varepsilon'$. Let $Y = \tau^N T$ and $Y' = \tau^N T'$ have entries in $A_{\mathrm{inf}}$, let $g \in G_K$, and let $U \in M_d(C)$ and $U' \in M_{d'}(C)$ satisfy $U \theta(Y) = \theta(Y) \theta(\varepsilon(g))$ and $U' \theta(Y') = \theta(Y') \theta(\varepsilon'(g))$. Then all entries of $U$ and $U'$ have absolute value at most $B$. If also $n \geq 0$, $\Pi \in M_{d \times d'}(\mathbb{Z}_\ell)$ and $R \in M_{d \times d'}(\mathfrak{S})$ satisfy $\Pi \rho'(h) \equiv \rho(h) \Pi \pmod{\ell^n}$ for all $h \in G_K$ and $\Pi T' \equiv TR \pmod{\ell^n W(C^\flat)}$, then all entries of $U\Pi - \Pi U'$ have absolute value at most $B \ell^{-n}$.

Lean: `GlobalTheory.T.theta_conj_bounded_compatible_breuilKisin_frames`.

**Theorem 3.7.6 (Hodge-Tate jumps through a cover).** Let $L_0$ be a finite extension of $\mathbb{Q}_\ell$ in $\Omega$ with $\tau(K) \subseteq L_0$ for every embedding $\tau : K \to \Omega$, and let $a \geq 1$. Let $r : G_K \to \mathrm{GL}_a(\Omega)$ be a homomorphism, $\mathcal{C}$ a set of homomorphisms $G_K \to \mathrm{GL}_a(\Omega)$, and assume that $r$ has a cover over $L_0$ with members in $\mathcal{C}$. Let $J$ assign to each embedding $\tau : K \to \Omega$ a finite multiset $J(\tau)$ of integers. Assume that for every $\rho_1 \in \mathcal{C}$ and every realization $R_1$ of $\rho_1$ over a finite extension $L \supseteq L_0$, $R_1$ is semistable and $m_\tau(R_1, n)$ is the multiplicity of $n$ in $J(\tau)$ for every $\tau : K \to L$ and $n \in \mathbb{Z}$. Let $R$ be a realization of $r$ over a finite extension $L \supseteq L_0$. Then:

1. $R$ is de Rham;
2. $m_\tau(R, n)$ is the multiplicity of $n$ in $J(\tau)$ for every $\tau : K \to L$ and every $n \in \mathbb{Z}$;
3. if every realization of every member of $\mathcal{C}$ over every finite extension of $L_0$ is crystalline, then $R$ is crystalline.

Lean: `GlobalTheory.CovClose.closed_of_cover`.

*Proof.* Fix a [Breuil-Kisin datum](/entry/exists-log-flat-pow-bst/) for $K$ and a [Frobenius period](/entry/semistable-period-frame/) $\tau_0$. By Fontaine's theorem, $B_{\mathrm{dR}}^{G_{K''}} = K''$ for every finite extension $K''$. Let $N$ be the largest $|h|$ for $h \in J(\tau)$ and $\tau : K \to \Omega$; there are finitely many embeddings, so $N$ exists.

For each $n$ let $V'_n = \mathbb{Q}_\ell^{d'_n}$ with $\rho'_n$. By the lemma on layers $V'_n$ is semistable, and crystalline under the hypothesis of 3. By the lemma on jumps of a layer, the jumps of $V'_n$ lie in the interval from $-N$ to $N$. Since $\rho'_n$ is continuous, the [theorem on frames of bounded height](/entry/exists-frame-sst/) gives a de Rham frame $F_n$ of height $N$ for $\rho'_n$, with basis $T_n$ and cocycle $\varepsilon_n$, which is crystalline when $V'_n$ is. The [theorem on limits of de Rham frames](/entry/limit-frame-exists/) gives a de Rham frame $F$ of height $N$ for $\rho$, with basis $T$ and cocycle $\varepsilon$, which is crystalline if every $F_n$ is, and such that for each $n$ there is $m \geq n$ with $T$ linked to $T_m$ through $\Pi_m$ modulo $\ell^n$. By the lemma on de Rham frames, $\mathbb{Q}_\ell^d$ with $\rho$ is de Rham, and by the lemma on reading de Rham and crystalline representations, $R$ is de Rham. This is 1. Under the hypothesis of 3, every $F_n$ is crystalline, hence $F$ is, hence $\mathbb{Q}_\ell^d$ is crystalline by the lemma on crystalline frames, and $R$ is crystalline by the lemma on reading. This is 3.

For 2, fix $\tau : K \to L$. The lemma on inverting an embedding gives $\sigma \in G$ with $\sigma(\tau(x)) = x$ for $x \in K$. Take $g$, $w$ and $z$ from the lemma on a Galois element; $z \neq 0$ since $z \theta(w) = 1$. For each $m$, [the lemma on Hodge bases of de Rham lattices](/entry/sst-periods/) gives a Hodge basis $H_m$ of $\rho'_m$ for $E$ over $K$, since $V'_m$ is semistable and so de Rham; the lemma on bounded poles gives $Y_m = \tau_0^N T_m$ over $A_{\mathrm{inf}}$; and the lemma on operators from de Rham frames gives $U'_m \in M_{d'_m}(C)$ with $U'_m \theta(Y_m) = \theta(Y_m) \theta(\varepsilon_m(g))$ and $U'_m \theta(V_{H_m}) = \theta(V_{H_m}) \, \mathrm{diag}(z^{p_i - q})$. In the same way we get a Hodge basis $H$ of $\rho$, a matrix $Y$ and $U \in M_d(C)$ for the frame $F$. The lemma on a uniform bound gives $B$ with all entries of $U$ and $U'_m$ bounded by $B$. For each $n$, take $m \geq n$ with $T$ linked to $T_m$ through $\Pi_m$ modulo $\ell^n$. Then $\Pi_m T_m \equiv T R_1 \pmod{\ell^n}$ for some $R_1$, and $\Pi_m \rho'_m(h) \equiv \rho(h) \Pi_m$ modulo $\ell^m$, hence modulo $\ell^n$. So the entries of $U \Pi_m - \Pi_m U'_m$ are bounded by $B \ell^{-n}$.

Put $S(n) = \sum_{h \in J(\tau)} z^{hn}$. We show that the traces of the layers equal $S(n)$. Fix $m$ and a member $\rho_k$ of the layer of $\rho'_m$, with field $L_k$. Since $\rho_k$ has entries in $L_k$, it has a realization $R_k$ over $L_k$, given by $r_k$. By hypothesis $R_k$ is semistable, so de Rham, and its multiplicities at the embedding $\tau_k : K \to L_k$ with the same values as $\tau$ (recall $\tau(K) \subseteq L_0 \subseteq L_k$) are given by $J(\tau)$. The lemma on Hodge bases at an embedding gives a Hodge basis $H_k$ of $\sigma \circ r_k = \sigma \circ \rho_k$ over some $K' \supseteq K$, and the multiset of the $p_i - q$ is $J(\tau)$. Let $W = \theta(V_{H_k})$, which is invertible, and $u_k = W \, \mathrm{diag}(z^{p_i - q}) \, W^{-1}$. Then $u_k W = W \, \mathrm{diag}(z^{p_i - q})$, so $u_k$ is a Hodge-Tate operator of $\sigma \circ \rho_k$ for $E$ with parameter $z$ by the lemma on Hodge-Tate operators, and $\mathrm{tr}(u_k^n) = \sum_i z^{(p_i - q)n} = S(n)$. Since $\rho_k$ reads $\rho'_m$ through $b^{(m)}_{\cdot, k}$ and $e^{(m)}$, the lemma on powers of the operator gives $u_k^n = \sum_i (U'^{\,n}_m e^{(m)})_i \, \sigma(b^{(m)}_{i,k})$. Taking traces, the hypothesis on layers in the lemma on traces holds.

Next, $S(0)$ is the size of $J(\tau)$. By the lemma that the first layer is not empty, the layer of $\rho'_1$ has a member. For a member $\rho_k$ of that layer, the case $n = 0$ above gives $S(0) = \mathrm{tr}(u_k^0) = a$. The lemma on traces along a cover now gives $\mathrm{tr} \big( \sum_i (U^n e)_i \, \sigma(b_i) \big) = S(n)$ for every $n$.

Finally, the lemma on Hodge bases at an embedding, applied to $R$, $\tau$ and $\sigma$, gives a Hodge basis $H_R$ of $\sigma \circ r$ over some $K'$ with $\#\{i : p_i - q = n\} = m_\tau(R, n)$. As above, $u = \theta(V_{H_R}) \, \mathrm{diag}(z^{p_i - q}) \, \theta(V_{H_R})^{-1}$ is a Hodge-Tate operator of $\sigma \circ r$, and $\mathrm{tr}(u^n) = \sum_i z^{(p_i - q)n}$. Since $r$ reads $\rho$ through $b$ and $e$, the lemma on powers of the operator, with $H$ and $U$, gives $u^n = \sum_i (U^n e)_i \, \sigma(b_i)$. So $\sum_i z^{(p_i - q)n} = S(n)$ for all $n \geq 0$. The lemma on power sums shows that the multiset of the $p_i - q$ is $J(\tau)$, and so $m_\tau(R, n)$ is the multiplicity of $n$ in $J(\tau)$. $\square$

**Remark 3.7.7 (Formalization).** The homomorphism $r$ is not assumed continuous; only the lattices $\rho$ and $\rho'_n$ of the cover are. The proof that $S(0) = a$ uses the layer of index $1$. The four lemmas on frames are not opened beyond their statements. The lemma on a uniform bound takes the first frame of a height $N'$ together with the equation $N' = N$. The lemma on operators from de Rham frames has a second part, on the divisibility of the matrices $A, A'$ of the frame by $E^{N - N_0}$, which is not used here, and the bound on the jumps in the lemma on Hodge bases of de Rham lattices is discarded. Fontaine's theorem is the field `invdR` of a fit of the model of period rings, chosen by `MemLoc.FitsEx.exists_fits`.

## Notes and references

The chapter feeds two results of the proof of [the Galois row](/proof/galois-row/). The theorem on [frames of bounded height](/entry/exists-frame-sst/) and the theorem on [limits of de Rham frames](/entry/limit-frame-exists/) are inputs of [the theorem on the core of the Galois row](/entry/core-all-of/), and the theorem on covers of this section is an input of [the theorem on closedness at $\ell$](/entry/closed-at-l/). Both lie under the step [the Galois row holds](/step/galois-row-holds/).

The frames of this chapter are a matrix form of Kisin's modules over $\mathfrak{S}$ attached to lattices in semistable representations. Kisin works with the nonnegative case, where the Frobenius has no inverse poles; here the jumps lie between $-N$ and $N$, so both the Frobenius and its inverse have poles of order at most $N$. Kisin's modules are constructed from the filtered $(\varphi, N)$-module through a ring of functions on the open unit disc; here they are built from explicit period matrices over $A_{\mathrm{cris}}$ and the disc rings $D_{\mathfrak{S}}$ and $D_A$. The passage to a limit of a tower of lattices, and the transfer of the de Rham property and of the jumps through a cover, have no single classical source that we know of.

- M. Kisin, *Crystalline representations and F-crystals*, in: Algebraic Geometry and Number Theory, Progr. Math. 253, Birkhäuser, 2006, §1 and §2.
- J.-M. Fontaine, *Le corps des périodes p-adiques*, Astérisque 223 (1994), Exposé II (the rings $A_{\mathrm{cris}}$, $B_{\mathrm{cris}}$, $B_{\mathrm{dR}}$, $B_{\mathrm{st}}$ and the theorem $B_{\mathrm{dR}}^{G_K} = K$).
- J.-M. Fontaine, *Représentations p-adiques semi-stables*, Astérisque 223 (1994), Exposé VIII (semistable, crystalline and de Rham representations, Hodge-Tate jumps).
- B. Bhatt, M. Morrow and P. Scholze, *Integral p-adic Hodge theory*, Publ. Math. IHÉS 128 (2018), §4 (Breuil-Kisin-Fargues modules over $A_{\mathrm{inf}}$).
