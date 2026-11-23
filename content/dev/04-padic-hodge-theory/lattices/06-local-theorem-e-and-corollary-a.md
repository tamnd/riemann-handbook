---
title: The local Theorem E and its corollary
decls:
  - Formalism.MainNotions.N.Ln03.local_theorem_of_inputs
  - Formalism.MainNotions.N.Ln03.corollary_local_exists_constant
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local Theorem E and its corollary

This section proves the local Theorem E at every prime, for every pair of finite extensions $K, L$ of $\mathbb{Q}_p$ and every ordering of the letters, together with a numerical bound on its exponent with the constant $800$. Then it derives the local form of Corollary A, a bound on the colength, with a constant $C_0$ that does not depend on the data. Both come from [Theorem E in lifting form](/entry/crystalline-lifting-second-form/) and [the realisation of the arc data](/entry/realised2-pf/), with the admitted inputs on Wach lattices. The corollary is used in [the closing of Corollary A](/entry/thm-ecor-a-closing/).

We work with a global datum $D$ that gives, at each prime $p$, a local theory: for finite extensions $K$ and $L$ of $\mathbb{Q}_p$ a period datum, a valuation $v$ on $L$ and the ring $\mathcal{O}_L$. With it come Wach data, Fontaine data and comparison data for $D$. In case A for $(K, L)$ at level $1$ the Wach data give a Wach datum $W_{K,L}$ at $(p, K, L)$ with $n = [K_0 : \mathbb{Q}_p]$ letters.

**Definition 8.6.1 (The bound of Theorem E).** Let $C \in \mathbb{R}$. The *bound of Theorem E with constant* $C$ holds if for every prime $p \ge 5$, all $n \ge 1$, $j, G, S, \eta, h \in \mathbb{N}$, kinds $\mathrm{ty}$, cuts $\mathcal{C}$ with lengths $\ell$ and $H_1, H_2 \colon \mathbb{Z}/n \to \mathbb{N}$ such that $\mathcal{C}$ is a set of cuts with lengths $\ell$, $g = \max(G, S, \eta, 1) \le h$, $H_k(i) \le 2h$ for all $i$, and $H_k(c + k') \le 2G$ for $c \in \mathcal{C}$ and $1 \le k' \le j$, the exponent of Theorem E satisfies
$$e \le C \Bigl( \frac{h}{(p-1)^{j+1}} + g \ell^* + \log_p h \Bigr).$$

The *local Theorem E with constant* $C$ holds for $D$ if, for every prime $p$, all finite extensions $K, L$ of $\mathbb{Q}_p$, every $n \ge 1$ and every $\mathrm{emb} \colon \mathbb{Z}/n \to \mathrm{Hom}_{\mathbb{Q}_p}(K_0, L)$, [Theorem E holds for](/entry/crystalline-lifting-second-form/) $\mathrm{emb}$, over the ring $\mathcal{O}_L$ and the valuation of $L$, and the bound of Theorem E with constant $C$ holds.

**Definition 8.6.2 (Corollary A for an ordering).** Let $C \in \mathbb{R}$ and let $\mathrm{emb}$ be an ordering. *Corollary A with constant* $C$ holds for $\mathrm{emb}$ if the following is true. Assume the letter conditions and $p \ge 11$. Let $F \colon T_1 \to T_2$ be a map of crystalline lattices that is onto, with $T_1$ of good coefficients, and let $r = \dim_L T_2 \otimes \mathbb{Q}$. Let $b, w, S, \eta, j \in \mathbb{N}$ with $1 \le j$ and $j + 1 \le n$, a sign $\mathrm{up}_i$ and a size $\mathrm{sz}_i$ at each letter. Call a letter *thick* if $b \le \mathrm{sz}_i \le b + \eta$. Assume:

1. the jumps of $T_1$ at $i$ lie in $[\mathrm{sz}_i, \mathrm{sz}_i + S] \cup [-\eta, \eta]$ if $\mathrm{up}_i$ holds, and in $[-\mathrm{sz}_i - S, -\mathrm{sz}_i] \cup [-\eta, \eta]$ otherwise;
2. each letter is thick or has $\mathrm{sz}_i \le w$, and $C (j + 1)(w + S + \eta + 1) \le b$;
3. the thick letters come in *clusters of reach* $j$: for each thick $t$, either none of $t - 1, \dots, t - j$ is thick, or there is $d$ with $1 \le d \le j$, $t - d$ thick, and $t - k$ not thick for $1 \le k \le d + j$, $k \ne d$.

Put $h_C = b + \eta + S$ if some letter is thick and $h_C = w + S + \eta$ otherwise. Then
$$\begin{aligned} \operatorname{col}(F) \le C (n + 1) r \Bigl( &\frac{h_C}{(p-1)^{j+1}} + (w + S + \eta + 1)(j + 1) \\ &+ \log_p h_C \Bigr) \cdot \lambda. \end{aligned}$$
The *local Corollary A with constant* $C$ holds for $D$ if Corollary A with constant $C$ holds for every $p$, $K$, $L$, $n$ and $\mathrm{emb}$.

Here $\operatorname{col}(F)$ and $\lambda = \operatorname{length}(\mathcal{O}/p\mathcal{O})$ are as in [the first section](/entry/thm-b-at/).

**Theorem 8.6.3 (Local Theorem E from the admitted inputs).** Let $C \in \mathbb{R}$. Assume, for the data of $D$:

1. the properties P3, P4, P5, P6 and P9 of Wach lattices, the first property of Herr complexes, and the length lemma for Wach lattices;
2. the conclusion on Wach lattices whose first part gives $W_X$, and the constant result of Wach with constant $C$, which gives $W_R$;
3. in case A with $p \ge 5$: the tools and the level maps on the Hodge filtration, the saturation property, F1, F2, and a generator of $D(\mathbf{1})$;
4. Hodge exactness over every pair of finite extensions, and $D_{\mathrm{dR}} = D_{\mathrm{cris}}$ in case A;
5. the Fontaine core statement in case A, and a further input on the local situation.

Then the local Theorem E with constant $800$ holds for $D$.

Lean: `Formalism.MainNotions.N.Ln03.local_theorem_of_inputs`.

*Proof.* The bound of Theorem E with constant $800$ is a direct estimate of the exponent, proved without the inputs. For the lifting statement, fix $p$, $K$, $L$, $n$ and $\mathrm{emb}$, and assume the letter conditions and $p \ge 5$. Then $n = [K_0 : \mathbb{Q}_p]$, and $K \cong K_0$ lies in the maximal unramified extension of $\mathbb{Q}_p$. Let $L'$ be the compositum of $L$, a normal closure of $K_0(\mu_p)$ over $\mathbb{Q}_p$, and $\mathbb{Q}_p(\mu_{p^n})$. Then $(K, L')$ is in case A, and $L'$ contains a primitive $p^n$-th root of unity. Base change from $L$ to $L'$ holds for every local theory, and it keeps the jumps, the rank, the lifting exponents and the colength bounds. So it is enough to prove Theorem E over $L'$ for the ordering $\mathrm{emb}$ composed with $L \subseteq L'$. Both this ordering and the ordering of $W_{K,L'}$ satisfy $\mathrm{emb}_{i+1} \circ \sigma = \mathrm{emb}_i$, and the second is a bijection, so the first is a rotation $i \mapsto \mathrm{emb}_{i+a}$ of it; Theorem E passes to rotations. It remains to prove Theorem E for the ordering of $W = W_{K,L'}$, and we apply [Theorem E in lifting form](/entry/crystalline-lifting-second-form/). Its hypotheses: $s = 1$, $K_0 = K$ and $p \ge 5$ hold in case A; P5, P6, P9, the Herr property, $W_X$, $W_R$, the tools, F1, F2 and Hodge exactness are inputs; $\mathcal{O}_{L'}$ is the valuation ring of $v$ and is $p$-adically complete. Take the generator $e$ of $D(\mathbf{1})$. The Bloch-Kato extension property for $e$ follows from the Fontaine core statement and the input on the local situation. For the realisation we apply [the realisation of the arc data](/entry/realised2-pf/). The compatibilities of the level maps come from the comparison data. P3, P4, P5, P9, the level maps on the Hodge filtration, the saturation property, the length lemma, $D_{\mathrm{dR}} = D_{\mathrm{cris}}$ and the first part of Hodge exactness are inputs. $\mathcal{O}_{L'}$ is a discrete valuation ring with fraction field $L'$, $p$ lies in its maximal ideal since $p$ is not a unit, and it is complete for its maximal ideal. A unit $u \in \mathbb{Z}_p^\times$ with $v_p(u - 1) = 1$ whose image in $\mathcal{O}_{L'}$ is $\chi_\Gamma(\gamma)$ exists: take the cyclotomic character of a lift of $\gamma$ to $G_K$. The trivial lattice $\mathbf{1}$ is crystalline. $\square$

**Corollary 8.6.4 (Local Corollary A with a uniform constant).** There is $C_0 \in \mathbb{R}$ with the following property. Let $D$, its data and $C \in \mathbb{R}$ satisfy the hypotheses of the last theorem, and assume also the bound on generators of finite cohomology: for every $p$, $K$, $L$ with $K_0 \to K$ a bijection and every crystalline lattice $T$, the finite classes of $T$ are generated over $\mathcal{O}$ by at most $([K_0 : \mathbb{Q}_p] + 1) \dim_L T \otimes \mathbb{Q}$ elements. Then the local Theorem E with constant $800$ holds for $D$, and the local Corollary A with constant $C_2$ holds for $D$ for every $C_2 \ge C_0$.

Lean: `Formalism.MainNotions.N.Ln03.corollary_local_exists_constant`.

*Proof.* We use the following passage from Theorem E to Corollary A, proved in the chapter: there is $C' \ge 1$ such that for every $D$ and every $C_1 \ge 0$, the local Theorem E with constant $C_1$, the bound on generators, and the transfer of windows imply the local Corollary A with constant $\max(C', 4 C_1)$. Here the *transfer of windows* says that for a map onto $F \colon T_1 \to T_2$ of crystalline lattices, if the jumps of $T_1$ at a letter lie in a set $A$, so do the jumps of $T_2$. Put $C_0 = \max(C', 3200)$. By [the last theorem](/entry/local-theorem-of-inputs/), the local Theorem E with constant $800$ holds. The transfer of windows follows from the first part of Hodge exactness: each jump of $T_2$ is a jump of $T_1$. So the local Corollary A holds with constant $\max(C', 4 \cdot 800) = C_0$. For $C_2 \ge C_0$ it holds with $C_2$: the factor that multiplies the constant is at least $0$, since $p \ge 11$ makes $\log_p h_C \ge 0$. $\square$

**Remark 8.6.5 (Formalization).** The local Theorem E with constant $C$ is `Conclusion1 D C` = `LiftingTheoremLocalTheory D.loc C`, and the local Corollary A is `Conclusion2 D C` = `LocalCorollaryLifting D.loc C` ([WachCoordinates.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/WachCoordinates.lean#L316)); there are many other definitions named `Conclusion1` and `Conclusion2` in the library. The bound of Theorem E is `ThmEBound`, proved as `thmEBound_holds` (BoundedNumeratorPowerSummability.lean line 154), so the constant $800$ does not depend on any input. Base change is `base_change_every_theory`, a proved result, and the passage to $L'$ is `lift_of_caseA_rich` (LocalCorollaryOfDeRham.lean). The constant result of Wach is `ArchimedeanSignatureMatching D HW F C`, defined as `LiftingTheory.WachResultConstant D HW F C` (WachCoordinates.lean line 326): its name has nothing to do with its content. The constant $C$ of the theorem is free; it enters only there. The further input on the local situation is `LocalSituation.adm9`, the Fontaine core statement is `LitFont`; we did not unfold them, nor `adm3`, `Pr2a`, `lem3`, `coreWX`, `coreWR`. `local_theorem_of_inputs` runs with `maxHeartbeats 1000000` (LocalTheoremOfInputs.lean line 24). The constant $C_0 = \max(C', 3200)$ of the corollary is not explicit, since $C'$ comes from an existence statement (`corollary_of_Theorem_E`, BoundedNumeratorPowerSummability.lean line 722).
