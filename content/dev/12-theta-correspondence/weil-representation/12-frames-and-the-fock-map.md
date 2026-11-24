---
title: Frames and the Fock map
decls:
  - GlobalTheory.HoweD.FockData.exists_fock_data
  - GlobalTheory.T.exists_frames_fockMap_polynomial_lie_actions
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Frames and the Fock map

This section proves the input that the proof of [Howe duality at the real places](/entry/howe-duality-real-holds/) takes from the analysis of the Weil representation: at each infinite place the Hermitian space and the skew-Hermitian space have frames adapted to the given Cartan involutions, and these frames give an injective linear map from a tensor product of polynomial rings onto the space $\mathcal{P}_\infty$ of polynomial Fock vectors, under which the two unitary Lie algebras act by the explicit Fock operators of the [Fock space](/entry/howe-duality-real-holds/) up to multiples of the trace. Section 05 uses the theorem in the first step of its proof, and section 06 describes the space $\mathcal{P}_\infty$.

### Frames

Let $p, q \in \mathbb{N}$ and $I_{p,q} = \{1, \dots, p\} \sqcup \{1, \dots, q\}$ as in section 05. Let $J_{p,q}$ be the diagonal matrix on $I_{p,q}$ with entry $1$ on the positive part and $-1$ on the negative part.

**Definition 1.12.1 (Frame).** Let $M$ be a complex $n \times n$ matrix. A *frame* for $M$ of signature $(p, q)$ is a complex matrix $A$ of size $n \times (p+q)$, with columns indexed by $I_{p,q}$, such that
$${}^tA\, M\, \bar A = J_{p,q}$$
and $A$ has a right inverse.

If $M$ is Hermitian and nondegenerate, a frame is an orthonormal basis of $\mathbb{C}^n$ for the form $(x, y) \mapsto {}^tx M \bar y$, with $p$ vectors of norm $1$ and $q$ vectors of norm $-1$. So $p + q = n$ and $(p, q)$ is the signature of $M$.

**Definition 1.12.2 (Cartan involution).** Let $M$ be a complex $n \times n$ matrix. A matrix $\theta$ is a *Cartan involution* for $M$ if $\theta^2 = 1$, ${}^t\theta\, M\, \bar\theta = M$, and
$$\operatorname{Re}\big({}^t(\theta x)\, M\, \bar x\big) > 0 \quad \text{for all } x \in \mathbb{C}^n \setminus \{0\}.$$

For a Hermitian $M$ the conditions say that $\theta$ preserves the form and that the twisted form $(x, y) \mapsto {}^t(\theta x) M \bar y$ is positive definite. Then the $(+1)$ eigenspace of $\theta$ is a positive definite subspace and the $(-1)$ eigenspace is a negative definite subspace, and the two are orthogonal. A frame $A$ with $\theta A = A J_{p,q}$ is a frame whose positive columns lie in the $(+1)$ eigenspace and whose negative columns lie in the $(-1)$ eigenspace. Such a frame is said to be *adapted* to $\theta$.

### The setting

Let $F$ be a totally real number field and $E/F$ a CM extension with complex conjugation $\sigma$. Let $\psi$ be a standard additive character of $\mathbb{A}_F/F$. Let $X$ be a Hermitian space of dimension $n$ over $E$ with Gram matrix $J_X$, so that $\sigma(J_{X,ji}) = J_{X,ij}$ and $\det J_X \neq 0$. Let $W$ be a skew-Hermitian space of dimension $d$ over $E$ with Gram matrix $J_W$, so that $\sigma(J_{W,ji}) = -J_{W,ij}$ and $\det J_W \neq 0$. Let $\omega$ be a Weil representation of $\mathrm{U}(X) \times \mathrm{U}(W)$ over the adeles for $\psi$ and splitting characters $\chi_X, \chi_W$, in a model on the Schwartz-Bruhat functions on $\mathbb{A}_F^{\,n \times d}$, as in section 05. Let $S_\infty$ be the archimedean Schwartz space and $\mathcal{P}_\infty \subset S_\infty$ the space of polynomial Fock vectors of section 06.

For each infinite place $w$ of $F$ choose an embedding $\tau_w$ of $E$ into $\mathbb{C}$ over $w$. Write $J_X^{\tau_w}$ and $J_W^{\tau_w}$ for the images of the Gram matrices. Choose Cartan involutions $\theta_{X,w}$ for $J_X^{\tau_w}$ and $\theta_{W,w}$ for $i J_W^{\tau_w}$. Since $W$ is skew-Hermitian, $iJ_W^{\tau_w}$ is Hermitian: the conjugate of $i$ is $-i$, so
$$\overline{(i J_W^{\tau_w})_{ji}} = -i\, \overline{J^{\tau_w}_{W,ji}} = -i \cdot (-J^{\tau_w}_{W,ij}) = (iJ_W^{\tau_w})_{ij}.$$

For functions $p, q, r, s$ from the infinite places to $\mathbb{N}$, let
$$\mathcal{T}(p,q,r,s) = \bigotimes_w \mathcal{P}(p_w, q_w, r_w, s_w),$$
the tensor product over the infinite places of the polynomial Fock spaces of section 05, with the actions $\pi_{1,w}$ of $\mathfrak{gl}_{p_w,q_w}$ and $\pi_{2,w}$ of $\mathfrak{gl}_{r_w,s_w}$ on the factor at $w$.

### Lie actions through frames

A one-parameter subgroup $\gamma \colon \mathbb{R} \to \mathrm{U}(X)(\mathbb{A}_F)$ that lives at the infinite places acts on $S_\infty$ through $\omega$. Its derivative at $0$ on a smooth vector is the action of an element of the Lie algebra. To compare this action with the Fock operators, we read $\gamma$ in the frames.

**Definition 1.12.3 (Generator in a frame).** Let $A = (A_w)_w$ be frames and $\gamma$ a one-parameter subgroup of $\mathrm{U}(X)(\mathbb{A}_F)$ supported at the infinite places. A family $Y = (Y_w)_w$, with $Y_w \in \mathfrak{gl}_{p_w, q_w}$, is the *generator of $\gamma$ in the frames $A$* if
$$\gamma(t)^{\tau_w} A_w = A_w \exp(t Y_w) \quad \text{for all } t \in \mathbb{R} \text{ and all } w.$$

**Definition 1.12.4 (Acts by Fock operators).** Let $\Phi \colon \mathcal{T}(p,q,r,s) \to S_\infty$ be linear, let $\pi_w$ be an action of $\mathfrak{gl}_{p_w,q_w}$ on $\mathcal{P}(p_w,q_w,r_w,s_w)$, and let $c_w \in \mathbb{C}$. The group $\mathrm{U}(X)$ *acts through $\Phi$ by $\pi + c\operatorname{tr}$ in the frames $A$* if, for each one-parameter subgroup $\gamma$ supported at the infinite places, each generator $Y$ of $\gamma$ in the frames $A$, and each $T \in \mathcal{T}$, the map $t \mapsto \omega(\gamma(t))\Phi(T)$ is differentiable at $0$ with derivative
$$\Phi\Big(\sum_w \big(\pi_w(Y_w) + c_w \operatorname{tr}(Y_w)\big) T\Big).$$
Here $\pi_w(Y_w) + c_w \operatorname{tr}(Y_w)$ acts on the factor at $w$ of $T$. The same definition applies to $\mathrm{U}(W)$ with frames $C$ for $iJ_W$.

The constants $c_w$ measure the difference between the actual action and the Fock operators. They come from the splitting characters $\chi_X$ and $\chi_W$, which twist the action of each unitary group by a character, and from the constant $\tfrac12 \delta_{ll'}$ in the Fock operators.

### The theorem

**Theorem 1.12.5 (Frames and the Fock map).** In the setting above, there are functions $p, q, r, s$ from the infinite places to $\mathbb{N}$, frames $A_w$ of signature $(p_w, q_w)$ for $J_X^{\tau_w}$, frames $C_w$ of signature $(r_w, s_w)$ for $iJ_W^{\tau_w}$, a linear map
$$\Phi \colon \mathcal{T}(p,q,r,s) \to S_\infty,$$
and constants $c_w, c'_w \in \mathbb{C}$, such that:

1. $\Phi$ is injective;
2. the image of $\Phi$ is $\mathcal{P}_\infty$;
3. $\mathrm{U}(X)$ acts through $\Phi$ by $\pi_1 + c \operatorname{tr}$ in the frames $A$;
4. $\mathrm{U}(W)$ acts through $\Phi$ by $\pi_2 + c' \operatorname{tr}$ in the frames $C$.

Lean: `GlobalTheory.HoweD.FockData.exists_fock_data` (also `GlobalTheory.T.exists_frames_fockMap_polynomial_lie_actions`, a second name).

This is the existence of the Fock model of the Weil representation of a real unitary dual pair. For one real place it is in G. B. Folland, *Harmonic Analysis in Phase Space*, Ann. of Math. Stud. 122 (1989), Chapter 4, where the oscillator representation is moved by the Bargmann transform to holomorphic functions and the Lie algebra of the symplectic group acts by quadratic expressions in multiplication and differentiation operators. The Bargmann transform is in V. Bargmann, *On a Hilbert space of analytic functions and an associated integral transform*, Comm. Pure Appl. Math. 14 (1961).

*Proof.* The proof has four steps.

First, frames. Fix an infinite place $w$. The matrix $J_X^{\tau_w}$ is Hermitian, since $\tau_w$ takes $\sigma$ to complex conjugation on a CM field, and it is nondegenerate. Diagonalize the Cartan involution $\theta_{X,w}$: its $(+1)$ and $(-1)$ eigenspaces are orthogonal and are positive and negative definite. An orthonormal basis of each eigenspace gives a frame $A_w$ of some signature $(p_w, q_w)$ with $\theta_{X,w} A_w = A_w J_{p_w,q_w}$. The same argument for the Hermitian matrix $iJ_W^{\tau_w}$, whose determinant $i^d \det J_W^{\tau_w}$ is nonzero, and for $\theta_{W,w}$ gives a frame $C_w$ of a signature $(r_w, s_w)$ with $\theta_{W,w} C_w = C_w J_{r_w,s_w}$.

Second, the map. Put $a = 1$ and $b = i$. Then $ab = i$, the matrices $A_w$ are frames for $aJ_X^{\tau_w}$, and the matrices $C_w$ are frames for $bJ_W^{\tau_w}$. The product $ab = i$ is the factor that relates the symplectic form $\operatorname{tr}_{E/F}$ of $X \otimes W$ to the Hermitian forms read in the frames. From these frames one builds an injective linear map $\Phi$ from $\mathcal{T}$ to $S_\infty$ with the following property. Let $u \in M_{n \times d}(\mathbb{A}_E)$ be supported at the infinite places, and write $u^{\tau_w} = A_w\, c_w\, {}^tC_w$ with $c_w$ a matrix on $I_{p_w,q_w} \times I_{r_w,s_w}$. Then the Heisenberg derivative of $t \mapsto \rho(tu)$ on $\Phi(T)$ is $\Phi$ applied to $\sum_w h(c_w) T$, where
$$h(c) = \sqrt{2\pi} \sum_l \big(c_l \uparrow_l - \epsilon_l\, \bar c_l \downarrow_l\big),$$
with the raising and lowering operators $\uparrow_l$, $\downarrow_l$ of section 05 and a sign $\epsilon_l$ that depends on whether $l$ is positive. So $\Phi$ intertwines the Heisenberg Lie algebra, read in the frames, with the creation and annihilation operators of the Fock space. This is the Bargmann picture: the vacuum goes to the constant polynomial $1$, and the Heisenberg derivatives go to multiplication by the variables and to differentiation.

Third, the Lie actions. The Weil representation $\omega$ is a representation of $\mathrm{U}(X) \times \mathrm{U}(W)$ that is compatible with the Heisenberg group: $\omega(g)\rho(u)\omega(g)^{-1} = \rho(gu)$, up to the twist by the splitting characters. Differentiate this relation along a one-parameter subgroup $\gamma$ of $\mathrm{U}(X)$ supported at the infinite places, with generator $Y$ in the frames $A$. The derivative of $\omega(\gamma(t))$ is an operator whose commutator with each Heisenberg derivative $D_u$ is $D_{Yu}$. In the Fock space, the operator $\pi_1(Y)$ has the same commutators with the operators $h(c)$, since $\pi_1(E_{ab})$ is a sum of products $\uparrow \downarrow$. An operator on the Fock space that commutes with all $h(c)$ is a scalar, since the Fock space is irreducible for the Heisenberg algebra. So the derivative of $\omega(\gamma(t))$ is $\Phi \circ (\pi_1(Y) + \lambda(Y)) \circ \Phi^{-1}$ for a linear form $\lambda$ on the Lie algebra. The Weil property of $\omega$ for the splitting character $\chi_X$ fixes this form at each place as $c_w \operatorname{tr}(Y_w)$. The same argument for $\mathrm{U}(W)$, with the frames $C$ and the splitting of the Weil representation on $\mathrm{U}(W)$, gives $\pi_2 + c' \operatorname{tr}$.

Fourth, the image. The image of $\Phi$ contains the image of $1 \in \mathcal{T}$, which is a Gaussian vacuum: the frames are adapted to the Cartan involutions, so the annihilation operators of the Fock space correspond to the operators $D_{u'} - iD_u$ of section 06. The image is stable under the Heisenberg derivatives by the second step, so it contains $\mathcal{P}_\infty$, which is the smallest such space. Conversely, $\mathcal{T}$ is spanned by the monomials, and each monomial is obtained from $1$ by raising operators, so each $\Phi(T)$ is obtained from the vacuum by Heisenberg derivatives and lies in $\mathcal{P}_\infty$. So the image of $\Phi$ is $\mathcal{P}_\infty$. $\square$

**Remark 1.12.6.** The signatures $(p_w, q_w)$ and $(r_w, s_w)$ depend on the place $w$, and the theorem allows this. For a definite space $X$ one has $q_w = 0$ at all $w$, and the Fock space at $w$ is the ring of polynomials in $p_w r_w + p_w s_w$ variables, with the positive variables in degree $r_w$ and the others in degree $s_w$. Then $\mathcal{P}(p,0,r,s)$ is the classical Fock model of the holomorphic discrete series side of the pair $(\mathrm{U}(p), \mathrm{U}(r,s))$.

**Remark 1.12.7 (Formalization).** The theorem is `exists_fock_data` in [ExistsFramesFockMapPolynomialLieActions.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFramesFockMapPolynomialLieActions.lean#L29), and the second name is a `first | exact` wrapper under `maxHeartbeats 1000000`. The steps of the proof are four results that the theorem cites: `exists_signatureOrthonormalFrame_eigen_of_cartanInvolution` (frames), `exists_fockMap_signatures_depend_on_place` (the map $\Phi$, with the Heisenberg property `IsFockMapD`), `firstMember_lieAction_fock_plus_trace` and `howeSplitting_acts_fockAction_plus_traceMultiples` (the two Lie actions), and `polynomialFockSpace_eq_range_fockMap_variable_signature` (the image). The sketch of steps two to four above gives the mathematics behind these names; their proofs are in other files. The Weil property of $\omega$ has three parts, and the proof uses the first two; the third part, the continuity of $\omega$, is discarded at line 61. The conclusion records the frames in the form `FramedD` with $a = 1$ and $b = i$, but it does not record the Heisenberg property of $\Phi$ or the adaptation $\theta A = AJ$; both are used inside the proof only.
