---
title: K-finite cusp forms as finite sums
decls:
  - GlobalTheory.CuspGK.cuspForm_mem_iSup_irreducible_gK
  - GlobalTheory.T.cuspForms_eq_iSup_irreducible_gK
  - GlobalTheory.CuspGK.exists_finite_sum_gelfandKirillov_multiplicity
  - GlobalTheory.T.cuspForm_gelfandKirillov_finite_decomposition
  - GlobalTheory.KFinCuspSum.kFinite_cusp_form_eq_sum_values
  - GlobalTheory.T.kFinite_cusp_form_finite_sum_expansion
status: drafted
drafted_by: writer@claude-opus-5-5
---
## K-finite cusp forms as finite sums

This section proves that a $K$-finite cusp form of a fixed archimedean type is a finite sum of values of multilinear maps on the discrete series modules at the real places. The proof has three steps. A $K$-finite cusp form lies in the sum of the irreducible $(\mathfrak g, K)$-submodules that it generates. Each such submodule is the image of a multilinear map on the discrete series modules. A finite sum of such images then contains the form. The result is the first step of the approximation of cusp forms by theta lifts of Fock vectors in [Theorem 3.2.2](/entry/exists-sum-approx-pure-cusp-form/).

We work over a CM extension $E/F$ of number fields and a Hermitian space $V$ over $E$. Let $G_V = \mathrm U(V)$ and let $G_V(\mathbb A)$ be its adelic points, as in [adelic points](/learn/groups/#adelic-points-and-compact-open-subgroups). The real places of $F$ are indexed by a set $\mathcal T$, and $\theta = (\theta_\tau)_{\tau \in \mathcal T}$ is a family of embeddings that identifies each archimedean completion with $\mathbb C$. We assume that $\theta$ is an admissible family in the sense of the datum. We fix the local inputs of [ThetaLocalInputs](/step/theta-local-inputs-def/) throughout the section.

**Definition 3.1.1 (Discrete series model).** A discrete series model $M$ for $V$ consists of the following data at each $\tau \in \mathcal T$: a Hilbert space $H_\tau$ with a representation $\pi_\tau$ of $G_V(\mathbb R_\tau)$, a frame $f_\tau \in G_V(\mathbb R_\tau)$, a sign pattern $\varepsilon_\tau$ and a parameter $\sigma_\tau$. Put

$$K_\tau = \{ g \in G_V(\mathbb R_\tau) : f_\tau\, g\, f_\tau^{-1} \in K(\varepsilon_\tau) \},$$

where $K(\varepsilon_\tau)$ is the standard maximal compact subgroup of the unitary group of the signature $\varepsilon_\tau$. Let $H_\tau^{\mathrm{fin}} = H(\varepsilon_\tau, \sigma_\tau)^{K\text{-fin}}$ be the space of $K_\tau$-finite vectors of the discrete series module with parameter $\sigma_\tau$.

So $K_\tau$ is a maximal compact subgroup of $G_V(\mathbb R_\tau)$, as in [maximal compact subgroups](/learn/groups/#reductive-groups-and-maximal-compact-subgroups), moved by the frame $f_\tau$. We have not unfolded the parameter $\sigma_\tau$ or the module $H(\varepsilon_\tau, \sigma_\tau)$.

Let $R(g)$ be right translation on functions on $G_V(\mathbb A)$ by an element $g$ of $G_V(\mathbb R_\tau)$, and let $R(X)$ be the derivative of right translation in the direction $X$ of the Lie algebra $\mathfrak g_\tau$ of $G_V(\mathbb R_\tau)$.

**Definition 3.1.2 ($K$-finite function).** A function $\psi$ on $G_V(\mathbb A)$ is $K$-finite if it lies in a finite-dimensional subspace $W$ such that $R(g) W \subseteq W$ for every $\tau$ and every $g \in K_\tau$.

**Definition 3.1.3 ($(\mathfrak g, K)$-submodule).** A subspace $A$ of the functions on $G_V(\mathbb A)$ is a $(\mathfrak g, K)$-submodule if $R(g) A \subseteq A$ for every $\tau$ and $g \in K_\tau$, and $R(X) A \subseteq A$ for every $\tau$ and $X \in \mathfrak g_\tau$. It is irreducible if $A \neq 0$ and the only $(\mathfrak g, K)$-submodules contained in $A$ are $0$ and $A$. For a function $\psi$, let $\langle \psi \rangle_{\mathfrak g, K}$ be the smallest $(\mathfrak g, K)$-submodule that contains $\psi$.

The smallest submodule exists because an intersection of $(\mathfrak g, K)$-submodules is one. A smooth automorphic function and a cusp form are as in [automorphic forms on adelic groups](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups) and [cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms). A function $\psi$ has type $\sigma_\tau$ at $\tau$ if it meets the type condition of the model at $\tau$; we have not unfolded this condition.

**Theorem 3.1.4 (Complete reducibility of a $K$-finite cusp form).** Let $M$ be a discrete series model for $V$. Let $\psi$ be a smooth automorphic cusp form on $G_V(\mathbb A)$ that is $K$-finite. Then

$$\psi \in \sum_{A} A,$$

where the sum runs over the irreducible $(\mathfrak g, K)$-submodules $A$ with $A \subseteq \langle \psi \rangle_{\mathfrak g, K}$.

Lean: `GlobalTheory.CuspGK.cuspForm_mem_iSup_irreducible_gK` (also `GlobalTheory.T.cuspForms_eq_iSup_irreducible_gK`, a second name).

*Proof.* Put $U = \langle \psi \rangle_{\mathfrak g, K}$. The Petersson inner product gives a Hermitian form $b$ on the functions on $G_V(\mathbb A)$. It is positive on $U$, since the functions of $U$ are cusp forms and so are square integrable. It is invariant under $R(g)$ for $g \in K_\tau$, and $R(X)$ is skew for $b$ for $X \in \mathfrak g_\tau$. Since $\psi$ is $K$-finite, there is a linear map $e$ with these properties: $e$ maps each $(\mathfrak g, K)$-submodule of $U$ into itself, $e^2 = e$ on $U$, $b(ex, y) = b(x, ey)$ for $x, y \in U$, the image $e(U)$ is finite-dimensional, and $e\psi = \psi$. Think of $e$ as the projection onto the finitely many $K$-types of $\psi$. Now let $A \subseteq U$ be a $(\mathfrak g, K)$-submodule. Its orthogonal complement in $U$ for $b$ is again a $(\mathfrak g, K)$-submodule. Indeed, if $f \in U$ is orthogonal to $A$, then $b(a, R(g) f) = b(R(g)^{-1} a, f) = 0$ and $b(a, R(X) f) = -b(R(X) a, f) = 0$ for $a \in A$. An abstract lemma of complete reducibility now applies. Let $N$ be a module with a family of submodules closed under intersection, with a positive Hermitian form on $N$ such that the orthogonal complement of each submodule is a submodule, and with a map $e$ as above. Then each vector of $N$ fixed by $e$ lies in the sum of the irreducible submodules of $N$. Apply it with $N = U$ and the vector $\psi$. $\square$

The next step writes each irreducible piece through the discrete series modules.

**Theorem 3.1.5 (Finite sum of multilinear maps).** Let $M$ be a discrete series model for $V$. Let $\psi$ be a smooth automorphic cusp form on $G_V(\mathbb A)$ that is $K$-finite and has type $\sigma_\tau$ at every $\tau$. Then there are $n \ge 0$, multilinear maps

$$F_l : \prod_{\tau \in \mathcal T} H_\tau^{\mathrm{fin}} \to \{ \text{functions on } G_V(\mathbb A) \}, \qquad 1 \le l \le n,$$

and vectors $u_l \in \prod_\tau H_\tau^{\mathrm{fin}}$ with the following properties.

1. For each $l$ and each $u$, the function $F_l(u)$ is smooth automorphic and cuspidal.
2. ($K$-equivariance.) Let $\tau \in \mathcal T$, $g \in K_\tau$, $u \in \prod H^{\mathrm{fin}}$ and $w \in H_\tau^{\mathrm{fin}}$ with $w = \pi_\tau(g) u_\tau$. Let $u'$ be $u$ with the entry at $\tau$ replaced by $w$. Then $F_l(u') = R(g) F_l(u)$.
3. ($\mathfrak g$-equivariance.) Let $\tau \in \mathcal T$, $X \in \mathfrak g_\tau$, and let $w$ be the derivative at $t = 0$ of $t \mapsto \pi_\tau(\exp tX) u_\tau$. Let $u'$ be as above. Then $F_l(u') = R(X) F_l(u)$.
4. $\psi(g) = \sum_{l = 1}^n F_l(u_l)(g)$ for all $g \in G_V(\mathbb A)$.

Lean: `GlobalTheory.CuspGK.exists_finite_sum_gelfandKirillov_multiplicity` (also `GlobalTheory.T.cuspForm_gelfandKirillov_finite_decomposition`, a second name).

*Proof.* By [Theorem 3.1.4](/entry/cusp-form-mem-i-sup-irreducible-g-k/), $\psi$ lies in the sum of the irreducible $(\mathfrak g, K)$-submodules of $\langle \psi \rangle_{\mathfrak g, K}$. An element of a sum of subspaces is a finite sum of elements of finitely many of them. Each irreducible $(\mathfrak g, K)$-submodule $A$ of $\langle \psi \rangle_{\mathfrak g, K}$ consists of cusp forms of type $\sigma_\tau$ at each $\tau$, since $\psi$ has these properties and they pass to the submodule that $\psi$ generates. By the isotypic decomposition of cusp forms of a fixed type, $A$ is contained in the span of the values of the multilinear maps with properties 1 to 3. So $\psi$ is in this span. An element of the span is a finite sum of values $F_l(u_l)$, since a scalar multiple of a value $F(u)$ is the value of the multilinear map $cF$. $\square$

The two inputs of the proof, that irreducible submodules of a cusp form of type $\sigma$ have type $\sigma$ and the isotypic decomposition, are proved from the local inputs; we have not opened their proofs.

We now pass to the nodes of a grid. A grid $G$ over a real datum $R$ has at each node $(i, j)$, $0 \le i, j \le m$, a Hermitian space $V_{ij}$ with a discrete series model $M_{ij}$. A cusp form of the type of the node is a function on $G_{V_{ij}}(\mathbb A)$ that is smooth automorphic, cuspidal, and of type $\sigma_\tau$ at every $\tau$ for the model $M_{ij}$. We write $\mathrm{Vec}(M_{ij})$ for the space of global vectors of the model, and we call a map $T$ from $\mathrm{Vec}(M_{ij})$ to the functions on $G_{V_{ij}}(\mathbb A)$ admissible if it is a multilinear map of the model with no extra places and level $1$. We have not unfolded the space of global vectors or the admissibility condition.

**Theorem 3.1.6 (Finite sum expansion at a node).** Let $R$ be a real datum that meets the base conditions of the rows, and let $G$ be a grid for $R$ whose arrows meet the grid conditions. Let $0 \le i, j \le m$. Let $\psi$ be a cusp form of the type of the node $(i, j)$ that is $K$-finite. Then there are $n \ge 0$, admissible maps $T_1, \ldots, T_n$ and vectors $v_1, \ldots, v_n \in \mathrm{Vec}(M_{ij})$ with

$$\psi(g) = \sum_{l = 1}^n T_l(v_l)(g) \qquad \text{for all } g \in G_{V_{ij}}(\mathbb A).$$

Lean: `GlobalTheory.KFinCuspSum.kFinite_cusp_form_eq_sum_values` (also `GlobalTheory.T.kFinite_cusp_form_finite_sum_expansion`, a second name).

*Proof.* The base conditions on $R$ include that the family $\theta$ is admissible. So [Theorem 3.1.5](/entry/exists-finite-sum-gelfand-kirillov-multiplicity/) applies to $\psi$ and the model $M_{ij}$. It gives multilinear maps $F_l$ and vectors $u_l$ with $\psi = \sum_l F_l(u_l)$. By the globalization lemma for the local inputs, each $F_l$ with properties 1 to 3 extends to an admissible map $T_l$ on global vectors, such that for each $u$ there is a vector $v$ with $T_l(v) = F_l(u)$. Choose $v_l$ with $T_l(v_l) = F_l(u_l)$. Then $\psi = \sum_l T_l(v_l)$. $\square$

**Remark 3.1.7 (Formalization).** The names of the first two theorems say "eq" and "gelfandKirillov". The first statement is a membership, not an equality of spaces. The words "Gelfand-Kirillov" and "gK" name $(\mathfrak g, K)$-modules here; they have nothing to do with the Gelfand-Kirillov dimension. In the third theorem the grid conditions are not used; of the base conditions on $R$ only the admissibility of $\theta$ is used. The abstract lemma of complete reducibility is in [AbstractCompleteReducibilityStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/AbstractCompleteReducibilityStatement.lean#L5); we did not open the proof that it calls.
