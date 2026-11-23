---
title: The image of the dual exponential map
decls:
  - GlobalTheory.ExpImage.expStar_image
  - GlobalTheory.T.dualExp_teichmuller_power_sum_formula
  - GlobalTheory.ExpImage.expStar_levSum
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The image of the dual exponential map

A continuous cocycle $z : G_{K_s} \to \mathbb{Q}_\ell(-e)$ has a dual exponential: an element $\alpha \in K_s$ such that, in the graded piece of degree $e$ of $B_{\mathrm{dR}}$, the class of $z$ is the class of $\alpha t^e \log \chi$. This section proves that every element of $\ell^{\beta} \mathcal{O}_{K_s}$ is the dual exponential of a cocycle with values in $\mathbb{Z}_\ell$, for an explicit integer $\beta = \beta(s, e)$. The cocycles are built from Teichmüller lifts of roots of unity in $A_{\inf}$. The result is used in the next section: it lets us subtract from a given cocycle a cocycle with the same dual exponential, so that the difference has dual exponential $0$ and so is crystalline. We use [Fontaine's period rings](/learn/padic-hodge/#crystalline-and-semistable-representations) ([[Fontaine's period rings|K6HW8YWCQJ]]) and the [cyclotomic character](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules).

We keep the notation of the previous sections. Fix a prime $\ell$ and local period data at $\ell$ that is tied to its $A_{\inf}$ data. Let $\Omega$ be the algebraic closure of $\mathbb{Q}_\ell$ and $C$ its completion. The data give the cyclotomic character $\chi : G_{\mathbb{Q}_\ell} \to \mathbb{Z}_\ell^\times$, the ring $B$ with its map $\iota : B \to B_{\mathrm{dR}}$, the filtration $\mathrm{Fil}^\bullet$ of $B_{\mathrm{dR}}$, the element $t = \iota(t_B)$ of $\mathrm{Fil}^1$, the action of $G_{\mathbb{Q}_\ell}$ on $B_{\mathrm{dR}}$, the Frobenius $\sigma$ of $K_0$, and a compatible system of roots of unity $\zeta_j \in \Omega$ with $\zeta_j^{\ell^j} = 1$ and $\zeta_{j+1}^\ell = \zeta_j$. Let $K$ be a finite extension of $\mathbb{Q}_\ell$ and $K_j = K_0(\mu_{\ell^j})$. Let $s \geq 1$, with $s \geq 2$ if $\ell = 2$.

**Definition 6.8.1 (Normalized logarithm).** For $u \in \mathbb{Q}_\ell$ put
$$\log_\ell u = \frac{1}{\ell(\ell - 1)} \sum_{k \geq 0} \frac{(-1)^k \big(u^{\ell(\ell-1)} - 1\big)^{k+1}}{k + 1}.$$
For $g \in G_{\mathbb{Q}_\ell}$ let $\log \chi(g) = \log_\ell \chi(g)$ if $|\log_\ell \chi(g)| \leq 1$, and $\log \chi(g) = 0$ otherwise. So $\log \chi(g) \in \mathbb{Z}_\ell$.

Lean: `Formalism.MainNotions.LocalSituation.logZl` (also `Formalism.MainNotions.LocalSituation.logChi`, the map $\log \chi$).

**Definition 6.8.2 (Dual exponential condition).** Let $G \subseteq G_{\mathbb{Q}_\ell}$ be a subgroup, $e \in \mathbb{N}$, $z : G_{\mathbb{Q}_\ell} \to \mathbb{Q}_\ell$ a map and $\alpha \in \Omega$. We say that $z$ *has dual exponential $\alpha$ in weight $e$ on $G$* if:

1. $z$ is continuous on $G$ and $z(\sigma\tau) = z(\sigma) + \chi(\sigma)^{-e} z(\tau)$ for $\sigma, \tau \in G$;
2. there is $b \in \mathrm{Fil}^0 B_{\mathrm{dR}}$ such that for all $\sigma \in G$
$$z(\sigma) - \log \chi(\sigma) \cdot \alpha t^e - \big(\chi(\sigma)^{-e} \sigma(b) - b\big) \in \mathrm{Fil}^{e+1} B_{\mathrm{dR}}.$$

Lean: `GlobalTheory.Cyc.ExpStar`.

Condition 1 says that $z$ is a continuous cocycle with values in $\mathbb{Q}_\ell(-e)$. The element $t^e$ is fixed by the action $\sigma \cdot y = \chi(\sigma)^{-e} \sigma(y)$, so $\sigma \mapsto \log \chi(\sigma) \alpha t^e$ is a cocycle for this action when $\alpha \in K_s$ and $\sigma \in G_{K_s}$. Condition 2 says that $z$ and this cocycle have the same class in $H^1(G, \mathrm{Fil}^0 B_{\mathrm{dR}} / \mathrm{Fil}^{e+1})$ for the twisted action. By Tate's computation of $H^1(G_K, C)$ (J. Tate, *p-divisible groups*, §3), the class of $\log \chi$ spans the cohomology of the graded piece $\mathrm{Fil}^e / \mathrm{Fil}^{e+1}$ twisted by $\chi^{-e}$. So $\alpha$ is the coordinate of $z$ on this class.

**Definition 6.8.3 (Level sums).** Let $j \in \mathbb{N}$, let $T$ be a finite set, and let $c : T \to K_0$, $m : T \to \mathbb{N}$ and $d \in K_0$. The *level sum* is
$$S_s^j(c, m, d) = \sum_{i=0}^{s-1} \ell^{ji} \sum_{a \in T} \sigma^i(c_a)\, m_a^j\, \zeta_s^{m_a \ell^i} + \ell^{sj} d \in \Omega.$$
Let $P_s = \{ a < \ell^s : \ell \nmid a \}$. For $\lambda : \mathbb{N} \to K_0$ put $\Lambda_s^e(\lambda, d) = S_s^e(\lambda|_{P_s}, \mathrm{id}, d)$, that is
$$\Lambda_s^e(\lambda, d) = \sum_{i=0}^{s-1} \ell^{ei} \sum_{a \in P_s} \sigma^i(\lambda_a)\, \zeta_s^{a \ell^i} + \ell^{se} d.$$

Lean: `GlobalTheory.ExpImage.levSum` (also `GlobalTheory.ExpImage.cycVal`, the sum $\Lambda_s^e$, and `GlobalTheory.ExpImage.primeTo`, the set $P_s$).

Since $c_a$, $d$ and $\zeta_s$ lie in $K_s$, every level sum lies in $K_s$.

**Definition 6.8.4 (The exponent $\beta$).** Put $\beta(s, 0) = -1$ and, for $e \geq 1$,
$$\beta(s, e) = s - 1 - e - v_\ell\big((e-1)!\big).$$

Lean: `GlobalTheory.Cyc.betaE`.

**Lemma 6.8.5 (Dual exponential of a level sum).** Let $e \in \mathbb{N}$ and let $g \in G_{K_s}$ with $\chi(g) = 1 + \ell^s$. Let $T$ be a finite set, $c : T \to K_0$ and $m : T \to \mathbb{N}$, with $|c_a| \leq 1$ and $\ell \nmid m_a$ for $a \in T$. Let $d_0, d_1, \dots$ be elements of $K_0$ such that for every $j \leq e$
$$|d_j| \leq 1, \qquad d_j - \ell^j \sigma(d_j) = \sigma^s\Big( \sum_{a \in T} c_a m_a^j \Big).$$
Then there is $z : G_{\mathbb{Q}_\ell} \to \mathbb{Q}_\ell$ with $|z(\sigma)| \leq 1$ for $\sigma \in G_{K_s}$ such that $z$ has dual exponential
$$\frac{S_s^e(c, m, d_e)}{\log_\ell(1 + \ell^s) \cdot e! \cdot \ell^{se}}$$
in weight $e$ on $G_{K_s}$.

Lean: `GlobalTheory.ExpImage.expStar_levSum` (also `GlobalTheory.T.dualExp_teichmuller_power_sum_formula`, a second name).

*Proof.* Put $U = \chi(g)^{-e} \in \mathbb{Z}_\ell$. Since $\chi(g)^{-1} \equiv 1 \bmod \ell^s$, we have $\ell^s \mid U - 1$. Since $|\chi(g) - 1| = \ell^{-s}$, the element $g$ generates the level $s$ of the cyclotomic tower. Each $c_a$ is integral, so it lifts to $w_a \in A_{\inf}$ with image $c_a$ in $B$. Let $[\varepsilon^{(s)}] \in A_{\inf}$ be the Teichmüller lift of the root of unity at level $s$ in the tilt, given by the $A_{\inf}$ data. A result proved elsewhere in this development, applied with $M = e + 1$ and the conditions on $d_0, \dots, d_e$, gives $y \in A_{\inf}$ with
$$\begin{aligned} y - \varphi(y) &= \sum_{a \in T} w_a [\varepsilon^{(s)}]^{m_a}, \\ \iota(y) &\equiv \sum_{j=0}^{e} \frac{S_s^j(c, m, d_j)}{j!\, \ell^{sj}}\, t^j \pmod{\mathrm{Fil}^{e+1}}. \end{aligned}$$
Next, for each $a$ with $\ell \nmid m_a$, the power $[\varepsilon^{(s)}]^{m_a}$ solves a recursion that expresses the cocycle condition for $g$ and $U$ in $A_{\inf}$, again by a result proved elsewhere. The lifts $w_a$ are fixed by $G_{K_s}$ and by $H_\infty$, since both fix $K_0$. The recursion is stable under sums and under products with such fixed elements, so $y - \varphi(y)$ solves it. From the recursion, a third result gives $b \in \mathrm{Fil}^0 B_{\mathrm{dR}}$ such that $h(b) - b$ lies in $\mathbb{Z}_\ell + \mathrm{Fil}^{e+1}$ for every $h \in H_\infty$, and such that $\iota(y) + U g(b) - b$ lies in $\mathbb{Z}_\ell + \mathrm{Fil}^{e+1}$. With the expansion of $\iota(y)$, the element
$$\sum_{j=0}^{e} \frac{S_s^j(c, m, d_j)}{j!\, \ell^{sj}}\, t^j + \big(\chi(g)^{-e} g(b) - b\big)$$
lies in $\mathbb{Z}_\ell + \mathrm{Fil}^{e+1}$. The last step removes the terms of degree $j < e$: a fourth result proved elsewhere turns these two conditions on $b$ into a map $z$ with $|z| \leq 1$ on $G_{K_s}$ and dual exponential $(\log_\ell \chi(g))^{-1}$ times the coefficient of $t^e$ in weight $e$ on $G_{K_s}$. That coefficient is $S_s^e(c, m, d_e)/(e!\, \ell^{se})$, and $\chi(g) = 1 + \ell^s$. $\square$

**Theorem 6.8.6 (The image of the dual exponential contains a lattice).** Let $e \in \mathbb{N}$ and let $\alpha \in K_s$ with $|\alpha| \leq 1$. Then there is $z : G_{\mathbb{Q}_\ell} \to \mathbb{Q}_\ell$ with $|z(\sigma)| \leq 1$ for $\sigma \in G_{K_s}$ such that $z$ has dual exponential $\ell^{\beta(s, e)} \alpha$ in weight $e$ on $G_{K_s}$.

Lean: `GlobalTheory.ExpImage.expStar_image`.

*Proof.* Put $u = 1 + \ell^s$. It is a unit of $\mathbb{Z}_\ell$, since $s \geq 1$. The character $\chi$ maps the group $G_{K_0}$ of elements that fix $K_0$ onto $\mathbb{Z}_\ell^\times$, by a result proved elsewhere in this development. So there is $g \in G_{K_0}$ with $\chi(g) = u$. Since $\chi(g) \equiv 1 \bmod \ell^s$, the element $g$ fixes $\mu_{\ell^s}$, so $g \in G_{K_s}$. We have $|u - 1| = \ell^{-s}$ and $|\log_\ell u| = \ell^{-s}$.

First we reduce the claim to the sums $\Lambda_s^e$. Let $\rho \in \mathbb{Q}_\ell$ with $|\rho| = \ell^{(e+1)(s-1) - \beta(s, e)}$. Assume that for all $\lambda : \mathbb{N} \to K_0$ and $d \in K_0$ with $|\lambda_a| \leq 1$, $|d| \leq 1$ and
$$d - \ell^e \sigma(d) = \sigma^s\Big( \sum_{a \in P_s} \lambda_a \Big),$$
some $z$ with $|z| \leq 1$ on $G_{K_s}$ has dual exponential $\rho \Lambda_s^e(\lambda, d)$. Put $\kappa = \ell^{\beta(s,e)} / (\rho\, \ell^{(e+1)(s-1)})$. Then $|\kappa| = 1$, so $\kappa \alpha \in K_s$ and $|\kappa \alpha| \leq 1$. A result proved elsewhere in this development, on the decomposition of integral elements of $K_s$ along the cyclotomic basis, gives $\lambda$ and $d$ with the three properties above and with $\Lambda_s^e(\lambda, d) = \ell^{(e+1)(s-1)} \kappa \alpha$. Then $\rho \Lambda_s^e(\lambda, d) = \ell^{\beta(s,e)} \alpha$, and the assumption gives $z$.

It remains to find $\rho$ and to prove the assumption. For $e = 0$ take $\rho = (\log_\ell u)^{-1}$. Then $|\rho| = \ell^s = \ell^{(s-1) + 1}$, as required. Given $\lambda$ and $d$, apply the Lemma with $T = P_s$, $c = \lambda|_{P_s}$, $m = \mathrm{id}$ and $d_j = d$ for all $j$. The elements of $P_s$ are prime to $\ell$, and for $j = 0$ the condition of the Lemma is the condition on $d$. For $j = 0$ the level sum is $\Lambda_s^0(\lambda, d)$, so the Lemma gives the assumption. For $e \geq 1$, a result proved elsewhere in this development, the analogue of the Lemma in positive weight, gives $z$ with $|z| \leq 1$ on $G_{K_s}$ and dual exponential $\rho \Lambda_s^e(\lambda, d)$, with
$$\rho = \frac{u^e - 1}{\log_\ell u \cdot e! \cdot \ell^{se}}.$$
We have $|u^e - 1| = \ell^{-s - v_\ell(e)}$ and $v_\ell(e!) = v_\ell(e) + v_\ell((e-1)!)$. So $|\rho| = \ell^{se + v_\ell((e-1)!)}$. Since $(e+1)(s-1) - \beta(s, e) = es + v_\ell((e-1)!)$, this is the required norm. $\square$

**Remark 6.8.7 (Formalization).** The Theorem takes a datum `D` and uses its local theory `D.loc` with the $A_{\inf}$ data `D.locA` and the tie `D.locT`; the Lemma takes the local theory, the $A_{\inf}$ data and the tie `LocTied` as separate arguments. The Lemma is used by the Theorem only for $e = 0$; for $e \geq 1$ the proof calls `GlobalTheory.T.cyclotomicTower_frobenius_formula_pos_weight` ([DualExponentialImageContainsLattice.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DualExponentialImageContainsLattice.lean#L99)). The second name of the Lemma is proved by `first | exact ...` under `maxHeartbeats 1000000`. The map $\log \chi$ is cut off to $0$ when $|\log_\ell \chi(g)| > 1$, so that it lands in $\mathbb{Z}_\ell$. The steps of the proofs that we did not open are `GlobalTheory.Cyc.finrank_Ks_and_chi_surjective`, `GlobalTheory.T.exists_cyclotomicFrobeniusTwistedValue_eq_pow_mul`, `GlobalTheory.T.exists_lifts_of_norm_le_one_alt`, `GlobalTheory.T.frobeniusSolution_expansion_mod_filtration`, `GlobalTheory.T.ainfCocycleSolution_teichmullerEpsilonRoot_pow`, `GlobalTheory.T.exists_deRham_element_of_cocycleRecursion` and `GlobalTheory.T.expStar_of_low_terms_removed`; we give only their statements. The recursion of the proof of the Lemma is `GlobalTheory.ExpImage.Solv`, which we did not unfold in the text.
