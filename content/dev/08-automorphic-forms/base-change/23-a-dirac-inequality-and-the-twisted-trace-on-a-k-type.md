---
title: A Dirac inequality and the twisted trace on a K-type
decls:
  - UpperTheory.RealTr.diracCh
  - UpperTheory.RealTr.diracW
  - UpperTheory.V.Z.GSp4Splitting.lowIso2
  - UpperTheory.V.Z.GSp4Splitting.coreG
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A Dirac inequality and the twisted trace on a K-type

The archimedean side of the twisted trace comparison for base change from $\mathbb{R}$ to $\mathbb{C}$ needs two facts about Harish-Chandra modules of $G = \mathrm{GL}_n(\mathbb{C})$ with the infinitesimal character of a finite-dimensional representation. First, the highest weights of $K$-types are bounded below by a Dirac inequality, and a $K$-type below a certain cone forces the $K$-type of the Lefschetz functions of Section 13 to occur. Second, the twisted trace of the involution that swaps the two factors of $\mathfrak{gl}_n \times \mathfrak{gl}_n$ on the multiplicity space of that $K$-type is $\pm 2^n$. Both feed the global trace identities below the step [EveryCharacter](/step/every-character/).

We keep the notation of Section 13: $K = U(n)$, and for a non-increasing $\lambda \in \mathbb{Z}^n$, $\chi_\lambda = (\chi_\lambda^+, \chi_\lambda^-)$ is the parameter of the representation of highest weight $\lambda$. As in Section 14, $\gamma_m(\chi^\pm)$ is the scalar of the Gelfand element of degree $m$ on the parameter $\chi^\pm$. Let $\rho \in \mathbb{R}^n$ be the vector with $\rho_a = \frac{n-1}{2} - (a - 1)$ for $1 \le a \le n$, and write $|x|^2 = \sum_a x_a^2$.

### Pairs of $\mathfrak{gl}_n$-actions

**Definition 7.23.1 (Pair).** Let $V$ be a complex inner product space. A pair on $V$ is two families $E^1_{ab}$, $E^2_{ab}$ ($1 \le a, b \le n$) of linear operators on $V$ such that each family satisfies the relations of the standard basis of $\mathfrak{gl}_n$,
$$[E_{ab}, E_{cd}] = \delta_{bc}E_{ad} - \delta_{da}E_{cb},$$
every $E^1_{ab}$ commutes with every $E^2_{cd}$, the operators $K_{ab} = E^1_{ab} + E^2_{ab}$ satisfy $K_{ab}^* = K_{ba}$, and $P_{ab} = E^1_{ab} - E^2_{ab}$ satisfy $P_{ab}^* = -P_{ba}$ (adjoints in the sense of the inner product, on $V$).

The family $K$ is the action of $\mathfrak{k} = \mathfrak{gl}_n$ and $P$ is the action of $\mathfrak{p}$, as for the complexified Lie algebra of $\mathrm{GL}_n(\mathbb{C})$. For a family $E$ put $(E^1)_{ab} = E_{ab}$, $(E^{m+1})_{ab} = \sum_c E_{ac}(E^m)_{cb}$, and let $\Gamma_m(E) = \sum_a (E^m)_{aa}$ be the Gelfand element of degree $m$. Put $\bar E^2_{ab} = -E^2_{ba}$. The pair has infinitesimal character $\chi_\lambda$ if $\Gamma_m(E^1) = \gamma_m(\chi_\lambda^+)$ and $\Gamma_m(\bar E^2) = \gamma_m(\chi_\lambda^-)$ as scalars, for all $m$. The family $K$ is locally finite if every vector lies in a finite-dimensional subspace stable under all $K_{ab}$. For $\nu \in \mathbb{R}^n$ the highest weight space $V^K_\nu$ is the space of $v$ with $K_{aa}v = \nu_a v$ for all $a$ and $K_{ab}v = 0$ for $a < b$.

For $x \in \mathbb{R}^n$ let $x^{\mathrm{dom}}$ be its non-increasing rearrangement. Put
$$L(\lambda) = |2(\lambda + \rho)|^2, \qquad s(\nu) = |(\nu - \rho)^{\mathrm{dom}} + \rho|^2.$$
Let $\mathbb{C}[\mathbb{R}^n]$ be the group algebra with basis $e^x$, $x \in \mathbb{R}^n$. Put $\mathrm{alt}(x) = \sum_{w \in S_n}\mathrm{sgn}(w)e^{x \circ w}$ and
$$c_\rho = e^\rho\prod_{a < b}\big(1 + e^{-(\varepsilon_a - \varepsilon_b)}\big),$$
where $\varepsilon_a$ is the $a$-th unit vector. Up to a factor, $c_\rho$ is the character of the spin module of the Clifford algebra of $\mathfrak{p}$.

### The Dirac inequality

**Theorem 7.23.2 (Dirac inequality, general form).** Let $\lambda \in \mathbb{Z}^n$ and let $(E^1, E^2)$ be a pair on $V$ with infinitesimal character $\chi_\lambda$ and locally finite $K$. Let $\nu, x \in \mathbb{R}^n$ with $V^K_\nu \ne 0$, $x$ strictly decreasing, and the coefficient of $e^x$ in $c_\rho \cdot \mathrm{alt}(\nu + \rho)$ nonzero. Then $L(\lambda) \le |x|^2$.

Lean: `UpperTheory.RealTr.diracCh`.

The proof uses four facts about representations of $\mathfrak{gl}_n$ on inner product spaces. Let $F$ be a family that satisfies the $\mathfrak{gl}_n$ relations with $F_{ab}^* = F_{ba}$.

1. (Weyl.) If $F$ is locally finite and $V^F_\nu \ne 0$, then $\nu_a - \nu_b \in \mathbb{N}$ for $a < b$, and there are a finite-dimensional $F$-stable $S$ with character $c = \sum_\mu \dim(S_\mu)e^\mu$ and $d \ne 0$ with $\mathrm{alt}(\rho)\,c = d\,\mathrm{alt}(\nu + \rho)$.
2. (Clifford matrices.) There are a finite set $J$, matrices $c_{ab}$ on $\mathbb{C}^J$ with $c_{ab}c_{de} + c_{de}c_{ab} = \delta_{bd}\delta_{ae}$ and $c_{ab}^* = c_{ba}$, and weights $\eta_j \in \mathbb{R}^n$, such that the spin operators $\mathrm{sp}_{ab} = \sum_d c_{ad}c_{db} - \delta_{ab}\frac n2$ have $\mathrm{sp}_{aa}$ diagonal with entries $\eta_j(a)$, and $\sum_j e^{\eta_j} = 2^n c_\rho$.
3. (Tensor product.) On $V \otimes \mathbb{C}^J$ the family $F_{ab} \otimes 1 + 1 \otimes \mathrm{sp}_{ab}$ satisfies the same conditions, and $S \otimes \mathbb{C}^J$ is stable with character $c\sum_je^{\eta_j}$.
4. (Multiplicities.) If $S$ is finite-dimensional and stable with character $c$, and $\kappa + \rho$ is strictly decreasing, then the coefficient of $e^{\kappa + \rho}$ in $\mathrm{alt}(\rho)\,c$ is $\dim(V^F_\kappa \cap S)$.

We also use the Dirac inequality on the tensor product: if $V \otimes \mathbb{C}^J$ has a nonzero highest weight space of weight $\kappa$ for the family of fact 3 built from $K$, then $L(\lambda) \le |\kappa + \rho|^2$. This is Parthasarathy's inequality in the present setting.

*Proof.* The family $K$ satisfies the $\mathfrak{gl}_n$ relations, because the two families of the pair do and commute, and $K_{ab}^* = K_{ba}$. Fact 1 gives $S$, $c$ and $d$. Fact 2 gives $J$, $c_{ab}$ and $\eta$, and fact 3 gives a stable subspace of $V \otimes \mathbb{C}^J$ with character $c\sum_je^{\eta_j} = 2^nc\,c_\rho$. Since $\mathbb{C}[\mathbb{R}^n]$ is commutative,
$$\mathrm{alt}(\rho)\,c\sum_je^{\eta_j} = 2^n d\; c_\rho\,\mathrm{alt}(\nu + \rho).$$
By fact 4 with $\kappa = x - \rho$, the dimension of the highest weight space of weight $x - \rho$ in $V \otimes \mathbb{C}^J$ is $2^nd$ times the coefficient of $e^x$ in $c_\rho\,\mathrm{alt}(\nu + \rho)$, which is nonzero. The Dirac inequality on the tensor product gives $L(\lambda) \le |x|^2$. $\square$

**Corollary 7.23.3 (Dirac inequality).** Under the hypotheses of the theorem on $\lambda$ and the pair, $V^K_\nu \ne 0$ implies $L(\lambda) \le s(\nu)$.

Lean: `UpperTheory.RealTr.diracW`.

*Proof.* By fact 1, $\nu$ is dominant. Put $x = (\nu - \rho)^{\mathrm{dom}} + \rho$. It is strictly decreasing, since $(\nu - \rho)^{\mathrm{dom}}$ is non-increasing and $\rho$ is strictly decreasing. For dominant $\nu$ the coefficient of $e^x$ in $c_\rho\,\mathrm{alt}(\nu + \rho)$ is $1$. The theorem gives $L(\lambda) \le |x|^2 = s(\nu)$. $\square$

### A $K$-type that occurs

**Definition 7.23.4 (Lefschetz $K$-type).** Let $\lambda \in \mathbb{Z}^n$ be non-increasing. A Lefschetz $K$-type for $\lambda$ is a finite-dimensional continuous unitary representation $(E, \tau)$ of $K$ with an operator $T$ that commutes with $\tau$ and satisfies $T^2 = 1$, such that for $k = \mathrm{diag}(z) \in K$ with the $z_a^2$ distinct,
$$\begin{aligned}\mathrm{tr}\,\tau(k) &= \prod_{a,b}(1 + z_a/z_b)\,\overline{\mathrm{ch}_\lambda(z)}^{\,2},\\ \mathrm{tr}\,\tau(k)T &= \prod_{a,b}(1 + z_a/z_b)\,\overline{\mathrm{ch}_\lambda(z^2)}.\end{aligned}$$

These are the traces of the bundle of Section 13. For a pair $(E^1, E^2)$ on $V$, a homomorphism $\sigma$ from $K$ to the linear maps of $V$ is a $K$-action of the pair if $\sigma$ is unitary and every vector lies in a finite-dimensional subspace stable under $\sigma$ and $K_{ab}$ on which $\frac{d}{dt}\sigma(e^{tX})|_{t=0} = \sum_{a,b}X_{ab}K_{ab}$ for skew-Hermitian $X$. Let $\mathrm{Hom}_K(E^\vee, V)$ be the space of linear maps $t \colon E^\vee \to V$ with $t(\xi \circ \tau(k)^{-1}) = \sigma(k)t(\xi)$.

Put $m_0(\lambda) = 2(\lambda + \rho)$. Let $H(\lambda)$ be the finite set of weights $2\lambda + 2r$, where $\{1, \dots, n\}$ is cut into consecutive blocks on which $\lambda$ is constant and $r_a$ is half the number of indices in later blocks minus half the number in earlier blocks.

**Theorem 7.23.5 (A $K$-type that occurs).** Let $\lambda$ be non-increasing, $(E, \tau, T)$ a Lefschetz $K$-type for $\lambda$, and $(E^1, E^2)$ a pair on $V$ with infinitesimal character $\chi_\lambda$ and a $K$-action $\sigma$, such that $\sigma$ is unitary, every vector lies in a finite-dimensional $\sigma$-stable subspace, and the matrix coefficients $k \mapsto \langle w, \sigma(k)v\rangle$ are continuous. Let $A$ be an isometry of $V$ with $A^2 = 1$, commuting with $\sigma$, and with $AE^1_{ab} = E^2_{ab}A$. Suppose that some $\nu \in \mathbb{R}^n$ has $V^K_\nu \ne 0$ and that $m_0(\lambda) - \nu$ is a combination of the roots $\varepsilon_a - \varepsilon_b$ ($a < b$) with coefficients in $\mathbb{N}$. Then $\mathrm{Hom}_K(E^\vee, V) \ne 0$.

Lean: `UpperTheory.V.Z.GSp4Splitting.lowIso2`.

*Proof.* The $K$-action makes $K$ locally finite. By fact 1, $\nu$ is dominant, hence non-increasing. The [Dirac inequality](/entry/dirac-w/) gives $L(\lambda) \le s(\nu)$; together with the cone condition on $m_0(\lambda) - \nu$, this forces $\nu \in H(\lambda)$. Next, the dual $E^\vee$ carries a $\mathfrak{gl}_n$-action $F$ that integrates $\tau^\vee$, and the trace of the dual of $T$ on the highest weight space $(E^\vee)^F_\nu$ is $2^n$ times a coefficient of a character product; for $\nu \in H(\lambda)$ this coefficient is $1$. A trace $2^n \ne 0$ forces $(E^\vee)^F_\nu \ne 0$. Pick nonzero $x \in (E^\vee)^F_\nu$ and $y \in V^K_\nu$. An extension lemma for highest weight vectors turns the linear map $(E^\vee)^F_\nu \to V^K_\nu$ that sends $x$ to $y$ into a $\mathfrak{gl}_n$-map $t \colon E^\vee \to V$ with $t(x) = y$. A $\mathfrak{gl}_n$-map between modules whose actions are the derivatives of the actions of $K$ commutes with $K$. So $t$ is a nonzero element of $\mathrm{Hom}_K(E^\vee, V)$. $\square$

### The twisted trace on the $K$-type

Now we strengthen the conditions on $V$. A core module for $\lambda$ is a pair $(E^1, E^2)$ on $V \ne 0$ with infinitesimal character $\chi_\lambda$ and a $K$-action $\sigma$, such that the algebra generated by all $E^i_{ab}$ moves each nonzero vector to every vector, together with an isometry $A$ with $A^2 = 1$, $A\sigma(k) = \sigma(k)A$ and $AE^1_{ab} = E^2_{ab}A$. The involution $A$ is the action of the outer automorphism that swaps the two factors of $\mathfrak{gl}_n \times \mathfrak{gl}_n$, that is, complex conjugation on $\mathrm{GL}_n(\mathbb{C})$. It acts on $\mathrm{Hom}_K(E^\vee, V)$ by $t \mapsto A \circ t \circ T^\vee$, where $T^\vee$ is the dual of $T$.

**Theorem 7.23.6 (Twisted trace on a $K$-type).** Let $\lambda$ be non-increasing, $(E, \tau, T)$ a Lefschetz $K$-type for $\lambda$ and $(E^1, E^2, \sigma, A)$ a core module for $\lambda$. If $\mathrm{Hom}_K(E^\vee, V)$ is finite-dimensional and nonzero, then the trace of $t \mapsto A \circ t \circ T^\vee$ on it is $s\,2^n$ with $s \in \{1, -1\}$.

Lean: `UpperTheory.V.Z.GSp4Splitting.coreG`.

The proof uses three inputs.

1. (Counting.) For each $\mu \in H(\lambda)$, the highest weight space $V^K_\mu$ is finite-dimensional and stable under $A$. If $\mathrm{Hom}_K(E^\vee, V) \ne 0$, then some $V^K_\mu$ with $\mu \in H(\lambda)$ is nonzero, and the twisted trace equals $2^n\sum_{\mu \in H(\lambda)}\mathrm{tr}(A \mid V^K_\mu)$.
2. (Multiplicity one.) There is $\mu_0 \in H(\lambda)$ with $V^K_\mu = 0$ for every other $\mu \in H(\lambda)$, and $\dim V^K_{\mu_0} \le 1$.
3. (Sign.) An involution of a line has trace $1$ or $-1$.

*Proof.* By input 1 some $V^K_\mu$ with $\mu \in H(\lambda)$ is nonzero, so by input 2 it is $V^K_{\mu_0}$ and it is a line. The sum in input 1 has the single term $\mathrm{tr}(A \mid V^K_{\mu_0})$, and input 3 makes it $\pm 1$. $\square$

**Remark 7.23.7 (Formalization).** The general Dirac inequality is [DiracCh.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/RealTraceClifford/DiracCh.lean#L19); facts 1 to 4 are `irrCh`, `clifEx`, `tenCh` and `mult`, and the inequality on the tensor product is `diracHW`, whose proof we did not unfold. The corollary is [DiracW.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/RealTraceClifford/DiracW.lean#L33), with the coefficient computed by `mSymm` and `aux₃` and the rearrangement facts `rearr`. Neither statement asks that $\lambda$ be non-increasing. The theorem on a $K$-type that occurs is [PartSum.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GL4GeometricSide/PartSum.lean#L82), with the statement `LowIso` in `InnerEq.lean` (line 127); the steps are `harm_of`, `lefData`, `harmDom`, `homSurj` and `derAt`, not unfolded. Its proof uses only the pair, the infinitesimal character and the $K$-action; the unitarity, finiteness and continuity conditions on $\sigma$ (`isK`) and the four conditions on $A$ are never used. The twisted trace theorem is [CoreG.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GL4GeometricSide/CoreG.lean#L17): `coreG_of` applied to `countG_holds`, `multG_of_multFor multiplicity_formula_holds` and `signOne`; the six other facts fed to `multG_of` are not unfolded. The trace on a subspace is defined as $0$ when the subspace is not stable. The namespace `GSp4Splitting` and the folder `GL4GeometricSide` do not describe these statements, which concern $\mathrm{GL}_n(\mathbb{C})$ for every $n$.
