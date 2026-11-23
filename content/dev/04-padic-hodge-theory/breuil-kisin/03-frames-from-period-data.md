---
title: Frames from period data
decls:
  - GlobalTheory.semistablePeriodFrame
  - GlobalTheory.T.exists_breuilKisinFrame_semistablePeriods
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Frames from period data

A lattice in a semistable representation of $G_K$ should give a module over $\mathfrak{S}$ with a Frobenius, as in the theory of Breuil and Kisin. This section constructs such a module from period data of the kind built in [the previous section](/entry/sst-periods/), but moved from $A_{\mathrm{cris}}$ to a ring of series that converge on a disc of radius $|\pi|$. The result is a *frame*: an invertible matrix $T$ over $W(C^\flat)$ whose columns are fixed by $G_\infty$, on which Frobenius acts through a matrix over $\mathfrak{S}$ with poles of bounded order along $E$, and on which all of $G_K$ acts through a matrix over $A_{\mathrm{inf}}$. The frame is de Rham, and it is crystalline when the cocycle of the period data is trivial. [The main theorem](/entry/exists-frame-sst/) of the next section applies this result. We keep the Breuil-Kisin datum of the first section, with $e = \deg E$. We write $E$ also for $\mathrm{ev}(E) \in A_{\mathrm{inf}}$, and $G_K$ acts on $W(C^\flat)$ and on matrices entrywise.

**Definition 3.3.1 (Series on a disc).** Let $A$ be a commutative ring, $u \in A$ and $r > 0$ a real number. For $y \in A[1/\ell]$, let $\|y\|$ be the infimum of the real numbers $s > 0$ such that $y$ is an $A$-linear combination of monomials $\ell^{a-c} u^b$ with $a, b, c \geq 0$ and $\ell^{c-a} r^b \leq s$. The ring $D(A, u, r)$ is the completion of $A[1/\ell]$ for this gauge, and $A \to D(A, u, r)$ is the natural map. Let $f : A \to A'$ be a ring map and $u' \in A'$, $r' > 0$. A *disc map over $f$* is a ring map $F : D(A, u, r) \to D(A', u', r')$ that agrees with $f$ on the image of $A$ and satisfies $\|F(x)\| \leq \|x\|$ for all $x$.

So a monomial $\ell^{-n} u^b$ has size $\ell^{n} r^b$: the ring $D(A, u, r)$ consists of the series in $u$ with coefficients in $A[1/\ell]$ that converge when $u$ is given the absolute value $r$. For $A = \mathbb{Z}_\ell[[u]]$ this is the ring of power series with bounded denominators that converge on the closed disc $|u| \leq r$.

Put $r_0 = \ell^{-1/e}$, which is the absolute value of $\pi$, and
$$D_{\mathfrak{S}} = D(\mathfrak{S}, X, r_0), \qquad D_A = D(A_{\mathrm{inf}}, [\pi^\flat], r_0).$$
We view matrices over $A_{\mathrm{inf}}$ and over $\mathfrak{S}$ (through $\mathrm{ev}$) as matrices over $D_A$. A disc map $D_A \to D_A$ over the Frobenius $\varphi$ of $A_{\mathrm{inf}}$ is called a Frobenius of $D_A$, and a disc map $D_A \to D_A$ over the action of $g \in G_K$ on $A_{\mathrm{inf}}$ is called an action of $g$ on $D_A$.

**Definition 3.3.2 (Frobenius period).** A *Frobenius period* for the Breuil-Kisin datum is an element $\tau \in A_{\mathrm{inf}}$ such that $\varphi(\tau) = E \tau$ and $\varphi(\tau) = \eta([\varepsilon'] - 1)$ for a unit $\eta$ of $A_{\mathrm{inf}}$ and an element $\varepsilon' \in \mathcal{O}_{C^\flat}$ with $(\varepsilon')^\sharp = 1$ that has an $\ell$-th root $\delta$ with $\delta^\sharp \neq 1$.

The condition on $\varepsilon'$ says that $\varepsilon'$ is a compatible system $(1, \zeta'_\ell, \zeta'_{\ell^2}, \dots)$ with $\zeta'_\ell$ a primitive $\ell$-th root of unity. So $\varphi(\tau)$ divides the element $[\varepsilon'] - 1$, whose logarithm is a period of $\mathbb{Z}_\ell(1)$, and the relation $\varphi(\tau) = E\tau$ says that $\tau$ twists the Frobenius by $E$.

**Lemma 3.3.3 (Existence of a Frobenius period).** Every Breuil-Kisin datum has a Frobenius period.

Lean: `GlobalTheory.BSP.exists_isPer`.

Fix a Frobenius period $\tau$.

**Definition 3.3.4 (Semistable period datum).** Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map. A *semistable period datum* for $\rho$ and $\tau$ consists of integers $N, c_1, c_2, c_3 \geq 0$, matrices $F, F' \in M_d(W)$ with $FF' = \ell^{c_3}$, matrices $X, X' \in M_d(\mathfrak{S})$ with $XX' = \ell^{c_2} E^{2N}$, matrices $W, W' \in M_d(D_A)$ with $WW' = \tau^{2N}$, and a map $\kappa : G_K \to M_d(D_A)$, with the following properties.

1. For every Frobenius $\Phi$ of $D_A$, $\ell^{c_1} \Phi(W X') = \varphi(E)^N \, W X' F$.
2. For every $g \in G_K$ and every action $\Gamma$ of $g$ on $D_A$, $(E\tau)^N \rho(g) \, \Gamma(W X') = g(E\tau)^N \, W X' \kappa(g)$.
3. $\kappa(g) = 1$ for $g \in G_\infty$.
4. For $g$ and $\Gamma$ as in 2, $E^{2N}$ divides each entry of $X' \kappa(g) \Gamma(X)$ in $D_A$.
5. For each $m \geq 0$ there are $k \geq 0$ and $\Lambda \in M_d(\mathfrak{S})$ with $\Lambda \equiv \ell^k \pmod{E}$ such that, for $g$ and $\Gamma$ as in 2, $E^m$ divides each entry of $\kappa(g) \Gamma(\Lambda) - \Lambda$ in $D_A$.

To read 1 and 2, put $Y = W X' / (E\tau)^N$ in a ring where $E\tau$ is a unit. Since $\varphi(E\tau)^N = \varphi(E)^N E^N \tau^N$, property 1 says $\varphi(Y) = \ell^{-c_1} Y F$, and property 2 says $\rho(g) \, g(Y) = Y \kappa(g)$. So the columns of $Y$ are $d$ vectors in the representation, tensored with the period ring, on which $\varphi$ acts through a matrix over $W$ and $G_K$ acts through $\kappa$. Property 3 says that they are fixed by $G_\infty$. Properties 4 and 5 are the analogues of properties 5 and 6 of [the theorem on period matrices](/entry/sst-periods/): the matrix $X$ removes the poles along $E$, and $\kappa$ is a coboundary modulo each power of $E$, after scaling. When $\kappa(g) = 1$ for all $g$, the vectors are fixed by all of $G_K$, as for a crystalline representation.

**Definition 3.3.5 (Breuil-Kisin basis and frame).** Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map and $N \geq 0$. A *Breuil-Kisin basis of height $N$* for $\rho$ is a matrix $T \in \mathrm{GL}_d(W(C^\flat))$ together with $A, A' \in M_d(\mathfrak{S})$ such that
$$AA' = E^{2N}, \qquad E^N \varphi(T) = T A, \qquad \rho(g) \, g(T) = T \quad \text{for } g \in G_\infty.$$
A *frame* of height $N$ for $\rho$ is a Breuil-Kisin basis of height $N$ together with a map $\varepsilon : G_K \to M_d(A_{\mathrm{inf}})$ such that $\rho(g) \, g(T) = T \varepsilon(g)$ for all $g \in G_K$. The frame is *de Rham* if for each $m \geq 0$ there are $k \geq 0$ and $\beta \in M_d(\mathfrak{S})$ with $\beta \equiv \ell^k \pmod{E}$ such that $E^m$ divides each entry of $\varphi(\varepsilon(g)) \, g(\beta) - \beta$ in $A_{\mathrm{inf}}$ for all $g \in G_K$. The frame is *crystalline* if $[\pi^\flat]$ divides each entry of $\varepsilon(g) - 1$ in $A_{\mathrm{inf}}$ for all $g \in G_K$.

The columns of $T$ are $G_\infty$-invariant vectors of $\mathbb{Z}_\ell^d \otimes W(C^\flat)$, with $G_K$ acting through $\rho$. Let $M$ be the $\mathfrak{S}$-module that they span. The relation $\varphi(T) = T \cdot A/E^N$ says that $\varphi$ maps $M$ into $E^{-N} M$. Since $AA' = E^{2N}$, the inverse of $A/E^N$ is $A'/E^N$, so the Frobenius and its inverse both have poles of order at most $N$ along $E$. Equivalently, $M$ with the Frobenius $E^N \varphi$, whose matrix is $A$, is a Breuil-Kisin module in the sense of Kisin: the cokernel of its linearization is killed by $E^{2N}$. The frame adds the statement that the $A_{\mathrm{inf}}$-span of the columns of $T$ is stable under all of $G_K$. The de Rham condition says that the cocycle $\varphi \circ \varepsilon$ is a coboundary modulo each power of $\ker \theta$, after scaling by $\ell^k$; this is how the de Rham property of the representation shows up on the frame.

**Theorem 3.3.6 (Frames from period data).** Let $\tau$ be a Frobenius period, let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map such that each $\rho(g)$ is invertible, and let $s$ be a semistable period datum for $\rho$ and $\tau$, with cocycle $\kappa$. Then there are $N \geq 0$ and a frame of height $N$ for $\rho$ that is de Rham, and that is crystalline if $\kappa(g) = 1$ for all $g \in G_K$.

Lean: `GlobalTheory.semistablePeriodFrame` (also `GlobalTheory.T.exists_breuilKisinFrame_semistablePeriods`, a second name).

The proof has four steps. Fix $\tau$, $\rho$ and $s$ as in the theorem, with $N_s$ the integer and $W$, $X$, $\kappa$ the matrices of $s$. A disc map $D_{\mathfrak{S}} \to D_A$ over $\mathrm{ev}$ is called a realization.

**Lemma 3.3.7 (A Breuil-Kisin basis from the period datum).** There are $N \geq 0$, a Breuil-Kisin basis $T$ of height $N$ for $\rho$, a matrix $Y \in M_d(A_{\mathrm{inf}})$ and an invertible matrix $Z \in M_d(D_{\mathfrak{S}})$ such that $Y = \tau^{N_s} T$ in $M_d(W(C^\flat))$ and $W \, i(Z) = Y$ in $M_d(D_A)$ for every realization $i$.

Lean: `GlobalTheory.T.exists_breuilKisinBasis_of_semistablePeriods`.

The matrix $Z$ is the change of basis over the disc: it turns the period matrix $W$, which has entries in $D_A$, into a matrix $Y$ with entries in $A_{\mathrm{inf}}$. This is the step where series that converge only on the disc are replaced by integral ones.

**Lemma 3.3.8 (Galois stability).** Let $N$, $T$, $Y$ and $Z$ be as in the last lemma. There is a frame of height $N$ for $\rho$ with Breuil-Kisin basis $T$ and some cocycle $\varepsilon$, such that
$$g(E)^{N_s} \, X \, i(Z) \, \varepsilon(g) = E^{N_s} \, \kappa(g) \, \Gamma\big(X \, i(Z)\big)$$
in $M_d(D_A)$ for all $g \in G_K$, every action $\Gamma$ of $g$ on $D_A$ and every realization $i$.

Lean: `GlobalTheory.T.semistablePeriods_breuilKisin_galoisStable`.

**Lemma 3.3.9 (The frame is de Rham).** Let $N$, $T$, $Y$ and $Z$ be as in the lemma on a Breuil-Kisin basis, and let $\varepsilon$ be the cocycle of a frame with basis $T$ that satisfies the relation of the lemma on Galois stability. Then the frame is de Rham.

Lean: `GlobalTheory.T.semistablePeriodFrame_isDeRham`.

**Lemma 3.3.10 (The frame is crystalline).** In the situation of the last lemma, if $\kappa(g) = 1$ for all $g \in G_K$, then the frame is crystalline.

Lean: `GlobalTheory.T.isCr_of_wSeed_alt`.

The relation in the lemma on Galois stability compares the two cocycles $\varepsilon$ and $\kappa$ through the matrix $X \, i(Z)$. The de Rham property of the frame comes from property 5 of the period datum, which makes $\kappa$ a coboundary modulo powers of $E$, and property 4, which bounds the poles of $\kappa$ after conjugation by $X$.

*Proof of the theorem.* The lemma on a Breuil-Kisin basis gives $N$, $T$, $Y$ and $Z$. The lemma on Galois stability extends $T$ to a frame of height $N$ whose cocycle $\varepsilon$ is related to $\kappa$ as stated there. By the lemma that the frame is de Rham, it is de Rham. If $\kappa(g) = 1$ for all $g$, the last lemma shows that it is crystalline. $\square$

**Remark 3.3.11 (Formalization).** The map $\rho$ in the theorem is only required to take invertible values; it need not be a homomorphism. The height $N$ of the frame comes from the lemma on a Breuil-Kisin basis and is not related to the integer $N_s$ of the period datum in the statement. The four lemmas of the proof (`exists_breuilKisinBasis_of_semistablePeriods`, `semistablePeriods_breuilKisin_galoisStable`, `semistablePeriodFrame_isDeRham`, `isCr_of_wSeed_alt`) are not unfolded here, and the readings of $Z$ and of the role of properties 4 and 5 are ours. Properties 1, 2, 4 and 5 of a period datum quantify over all disc maps over $\varphi$ and over $g$; the structure `WSeed` does not assert that such maps exist. The ring $D(A, u, r)$ is `BSP.Disc`, the completion of `Localization.Away ℓ` for the gauge seminorm built from the monomials. The period datum is the structure `BKLim.WSeed`, the Breuil-Kisin basis is `BKLim.Pre`, and the frame is `BKLim.Frame`, with the predicates `Frame.IsDR` and `Frame.IsCr`. The Frobenius period is `BK.IsPer`.
